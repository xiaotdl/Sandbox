#include <stdio.h>
#include <stdlib.h>
int main() {
    char *buffer= NULL;
    long bufsize;
    FILE *fp = fopen("foo.txt", "r");
    if (fp != NULL) {
        /* Go to the end of the file. */
        if (fseek(fp, 0L, SEEK_END) == 0) {
            /* Get the size of the file. */
            bufsize = ftell(fp);
            if (bufsize == -1) { /* Error */ }

            /* Allocate our buffer to that size. */
            buffer = malloc(sizeof(char) * (bufsize + 1));

            /* Go back to the start of the file. */
            if (fseek(fp, 0L, SEEK_SET) != 0) { /* Error */ }

            /* Read the entire file into memory. */
            size_t newLen = fread(buffer, sizeof(char), bufsize, fp);
            if (newLen == 0) {
                fputs("Error reading file", stderr);
            } else {
                buffer[newLen++] = '\0'; /* Just to be safe. */
            }
        }
        fclose(fp);
    }

    fwrite(buffer, bufsize, 1, stdout);

    free(buffer); /* Don't forget to call free() later! */
}
