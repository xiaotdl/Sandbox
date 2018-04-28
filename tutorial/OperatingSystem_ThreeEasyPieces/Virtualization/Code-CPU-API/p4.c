#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/wait.h>

// FILE *f = fopen("file.txt", "w");
// if (f == NULL)
// {
//     printf("Error opening file!\n");
//     exit(1);
// }
// 
// /* print some text */
// const char *text = "Write this to the file";
// fprintf(f, "Some text: %s\n", text);
// 
// /* print integers and floats */
// int i = 1;
// float py = 3.1415927;
// fprintf(f, "Integer: %d, float: %f\n", i, py);
// 
// /* printing single chatacters */
// char c = 'A';
// fprintf(f, "A character: %c\n", c);
// 
// fclose(f);

int
main(int argc, char *argv[])
{
	FILE *f = fopen("file.txt", "w");
	if (f == NULL)
	{
		printf("Error opening file!\n");
		exit(1);
	}

    int rc = fork();
    if (rc < 0) {
        // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
	// child: redirect standard output to a file
	// close(STDOUT_FILENO);
	printf("hello from child");
	// open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
	/*const char *text1 = "Write child to the file";*/
	/*fprintf(f, "Some text: %s\n", text1);*/
	/*fclose(f);*/

	// now exec "wc"...
        char *myargs[3];
        myargs[0] = strdup("wc");   // program: "wc" (word count)
        myargs[1] = strdup("p4.c"); // argument: file to count
        myargs[2] = NULL;           // marks end of array
		execvp(myargs[0], myargs);  // runs word count
    } else {
        // parent goes down this path (original process)
		const char *text2 = "Write parent to the file";
		fprintf(f, "Some text: %s\n", text2);
		fclose(f);
        int wc = wait(NULL);
    }
    return 0;
}
