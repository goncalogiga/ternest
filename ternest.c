#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>
#include <getopt.h>
#include <errno.h>

typedef struct type_args {
  char * show_opt;
} type_args;

void file_fail_test(FILE* f, const char * function, const int line)
{
  int errnum;

  if( f == NULL )
  {
    errnum = errno;
    fprintf(stderr, "Error: A file coudn't be open at %s (ternest.c:%d)\n",
        function , line);
    fprintf(stderr, "Value of errno: %d\n", errno);
    perror("Error printed by perror");
    fprintf(stderr, "Error opening file: %s\n", strerror( errnum ));

    exit(EXIT_FAILURE);
  }
}

void
start_config()
{
  char * birthdate  = calloc(32 , sizeof(char));
  char * student_id = calloc(32 , sizeof(char));
  char * browser    = calloc(32 , sizeof(char));
  int i = 0;

  puts("Please enter your birthdate (DDMMYYYY) : ");

  do {
  birthdate[i] = getchar();
  i++;
  } while(birthdate[i-1] != '\n' && i < 32 );
  birthdate[i-1] = '\0';

  if( i >= 32)
    goto OVERFLOW;
  i = 0;
  puts("Please enter your student number : ");

  do {
  student_id[i] = getchar();
  i++;
  } while(student_id[i-1] != '\n' && i < 32 );
  student_id[i-1] = '\0';

  if( i >= 32)
    goto OVERFLOW;
  i = 0;
  puts("Please enter your desired browser (Firefox or Chrome) : ");

  do {
  browser[i] = getchar();
  i++;
  } while(browser[i-1] != '\n' && i < 32 );
  browser[i-1] = '\0';

  if( i >= 32)
    goto OVERFLOW;

  goto CONTINUE;

  OVERFLOW: {
    puts("Exited to prevent overflow. No nasty stuff please.");
    exit(1);
  }

  CONTINUE: {

  FILE * config;
  char * config_path = calloc(100 , sizeof(char));
  sprintf(config_path,"%s/.ternest/user/config.txt",getenv("HOME"));
  config = fopen(config_path,"w");
  file_fail_test(config, __FUNCTION__ , __LINE__);
  free(config_path);

  fprintf(config, "dateNaissance = %s\n", birthdate);
  free(birthdate);
  fprintf(config, "codeEtudiant = %s\n", student_id);
  free(student_id);
  fprintf(config, "browser = %s\n", browser);
  free(browser);

  fclose(config);
  
  }
}

void
print_usage(void)
{
  puts(
  "Usage:\n"
  "DEFAULT        will check for new marks:\n"
  "--show=all     will show all your marks.\n"
  "--show=new     will show you your new marks.\n"
  "--config       to configurate ternest.\n"
  "--help\n");
}

void
parse_args(int argc, char **argv , type_args * args)
{
   args->show_opt = NULL;

   int c = 0;
   opterr = 0;
   const char * short_opt = "hs:";
   struct option long_opt[] =
   {
      {"help"  ,    no_argument,       NULL, 'h'},
      {"show"  ,    required_argument, NULL, 's'},
      {"config",    no_argument      , NULL, 'c'},
      {       0,                    0,    0,   0}
   };

   while((c = getopt_long(argc, argv, short_opt, long_opt, NULL)) != -1)
   {
      switch(c)
      {
      case -1:
      case 0:
      break;

      case 'h':
        print_usage();
        exit(0);
      case 'c':
        start_config();
        break;
      case 's':
        args->show_opt = optarg;
        break;

      case '?':
        if (optopt == 's')
          puts("Option --show requires an argument.");
        else if (isprint (optopt))
          fprintf (stderr, "Unknown option `--%c'.\n", optopt);
        else   printf("%d , %s , %s\n", argc , argv[1] , short_opt);
          fprintf (stderr, "Unknown option character `\\x%x'.\n", optopt);

        print_usage();
        exit(1);

      default:
        fprintf (stderr, "Unknown option character `%c'.\n", c);
        print_usage();
        exit(1);
      }
   }
}

int
parse_config(char * browser)
{

FILE * config;
char * config_path = calloc(100 , sizeof(char));
sprintf(config_path,"%s/.ternest/user/config.txt",getenv("HOME"));
config = fopen(config_path,"r");
file_fail_test(config, __FUNCTION__ , __LINE__);
free(config_path);

char * line = NULL;
size_t len = 0;
char c;
int count = 0;

for (size_t i = 0; i < 3; i++) {getline(&line,&len,config);}

while( count < strlen(line) )
{
  c = line[count];

  if( c == 'F' || c == 'f' )
  {
    free(line);
    fclose(config);
    return 1;
  }
  if(c == 'C' || c == 'c' )
  {
    free(line);
    fclose(config);
    return 2;
  }

  count++;
}

free(line);
fclose(config);

return 0;
}

int
main(int argc, char ** argv)
{
    char * browser = calloc(32,sizeof(char));
    type_args args;
    parse_args(argc, argv, &args);

    if( args.show_opt != NULL)
    {
      if( strcmp(args.show_opt,"new") == 0 )
        system("cat $HOME/.ternest/cache/new_marks.txt");
      else if ( strcmp(args.show_opt,"all") == 0 )
        system("cat $HOME/.ternest/user/your_marks.txt");
      else
      {
        puts("Invalid --show option.");
        print_usage();
      }

      free(browser);
      return 0;
    }

    if( parse_config(browser) )
        system("python3 $HOME/.ternest/webdrivers/webdriver_firefox.py");
    else if ( parse_config(browser) )
        system("python3 $HOME/.ternest/webdriver/webdriver_chrome.py");
    else
        puts("Unrecognized browser. Is your config set up?");

    free(browser);
    free(args.show_opt);

  return 0;
}
