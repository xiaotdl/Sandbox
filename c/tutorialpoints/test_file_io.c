/* A file represents a sequence of bytes. */

// fopen() -- opening files
// FILE *fopen( const char * filename, const char * mode  );

#include <stdio.h>

int main() {
    FILE *fp;

    // == writing a file ==
    // fputc()
    // fprintf()
    // fputs()
    fp = fopen("test_file_io.txt", "w+");
    fprintf(fp, "testing for fprintf...\n");
    fputs("testing for fputs...\n", fp);
    fclose(fp);

    // == reading a file ==
    // fgetc()
    // fscanf()
    // fgets()
    char buf[255];

    fp = fopen("test_file_io.txt", "r");

    fscanf(fp, "%s", buf);
    printf("fscanf: %s\n", buf);

    fgets(buf, 255, (FILE*)fp);
    printf("fgets : %s\n", buf);

    fgets(buf, 255, (FILE*)fp);
    printf("fgets : %s\n", buf);
}


