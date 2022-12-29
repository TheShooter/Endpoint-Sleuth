# Endpoint Sleuth

Endpoint Sleuth is an open source tool that helps developers and security professionals extract undocumented API endpoints from WAR, JAR or EAR packages based on JAX-RS Annotations for RESTful Web Services. When you're working on a new project and want to discover all the available endpoints, or you're conducting a security audit and need to identify any hidden or potentially vulnerable endpoints.

## Usage

To use Endpoint Sleuth, simply run the following command from the command line, replacing `[directory]` with the path to the Java file or directory you want to scan and [FILENAME] with filename of the results:

```bash
python3 endpoint_sleuth.py [-h] --path [directory] --filename [FILENAME] 

optional arguments:
  -h, --help           show this help message and exit
  --path PATH          The path to the decompiled EAR, JAR or WAR
  --filename FILENAME  the filename to save the output

```

Endpoint Sleuth will then search the specified file or directory for API endpoints and output the results to excelsheet file.

## Examples

Here's an example of Endpoint Sleuth in action:

```bash
user$ ./endpoint_sleuth.py --path myproject/com/project/ecommerce/rest

API Endpoints found:
[('users', 'POST'), ('users/file', 'POST'), ('users/export', 'PUT'), ('users/{userId}/linked-items', 'GET'), ('users/{userId}/linked-items', 'PUT'), ('users/{userId}/linked-categories', 'GET'), ('/health', 'GET')]

```

In this example, Endpoint Sleuth was run on the `myproject/com/project/ecommerce/rest` directory which contains .java files of a decompiled project called `myproject`, and it found these **API endpoints** along with their corresponding **request** **methods**.

## To-do

- [ ] Decompile WAR & EAR.
- [x] Save output to Excelsheet.
- [ ] Extract Params
- [ ] Test Extracted APIs
