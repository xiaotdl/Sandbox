#User Handbook
https://jenkins.io/doc/book/

## Installing Jenkins
https://jenkins.io/doc/book/installing/


## Using Jenkins

### Using credentials


## Pipeline
This chapter will cover all aspects of Jenkins Pipeline,
- running Pipelines
- writing Pipeline code
- extending Pipeline itself.

### What is Jenkins Pipeline?
Jenkins Pipeline (or simply "Pipeline" with a capital "P") is a suite of plugins which supports implementing and integrating continuous delivery pipelines into Jenkins.

### Declarative versus Scripted Pipeline syntax
Declarative and Scripted Pipelines are constructed fundamentally differently. Declarative Pipeline is a more recent feature of Jenkins Pipeline which:
- provides richer syntactical features over Scripted Pipeline syntax, and
- is designed to make writing and reading Pipeline code easier.

### Why Pipeline?
While Jenkins has always allowed rudimentary forms of chaining Freestyle Jobs together to perform sequential tasks, [4] Pipeline makes this concept a first-class citizen in Jenkins.

Building on the core Jenkins value of extensibility, Pipeline is also extensible both by users with Pipeline Shared Libraries and by plugin developers. [5]


### Pipeline concepts

*Pipeline*
A Pipeline is a user-defined model of a continuous delivery pipeline. A Pipeline’s code defines your entire build process, which typically includes stages for building an application, testing it and then delivering it.

Also, a pipeline block is a key part of Declarative Pipeline syntax.

*Node*
A node is a machine which is part of the Jenkins environment and is capable of executing a Pipeline.

Also, a node block is a key part of Scripted Pipeline syntax.

*Stage*
A stage block defines a conceptually distinct subset of tasks performed through the entire Pipeline (e.g. "Build", "Test" and "Deploy" stages), which is used by many plugins to visualize or present Jenkins Pipeline status/progress.

*Step*
A single task. Fundamentally, a step tells Jenkins what to do at a particular point in time (or "step" in the process). For example, to execute the shell command make use the sh step: sh 'make'. When a plugin extends the Pipeline DSL, [1] that typically means the plugin has implemented a new step.


### Pipeline syntax overview

The following Pipeline code skeletons illustrate the fundamental differences between Declarative Pipeline syntax and Scripted Pipeline syntax.

Be aware that both stages and steps (above) are common elements of both Declarative and Scripted Pipeline syntax.

#### *Declarative Pipeline fundamentals*
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //
            }
        }
        stage('Test') {
            steps {
                //
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}
"""

#### *Scripted Pipeline fundamentals*
In Scripted Pipeline syntax, one or more node blocks do/es the core work throughout the entire Pipeline. Although this is not a mandatory requirement of Scripted Pipeline syntax, confining your Pipeline’s work inside of a node block does two things:
1. Schedules the steps contained within the block to run by adding an item to the Jenkins queue. As soon as an executor is free on a node, the steps will run.
2. Creates a workspace (a directory specific to that particular Pipeline) where work can be done on files checked out from source control.
"""
Jenkinsfile (Scripted Pipeline)
node {
    stage('Build') {
        //
    }
    stage('Test') {
        //
    }
    stage('Deploy') {
        //
    }
}
"""

### Pipeline example
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make'
            }
        }
        stage('Test'){
            steps {
                sh 'make check'
                junit 'reports/**/*.xml'
            }
        }
        stage('Deploy') {
            steps {
                sh 'make publish'
            }
        }
    }
}
"""

### Getting Started with Pipeline

#### Defining a Pipeline
Both Declarative and Scripted Pipeline are DSLs [1] to describe portions of your software delivery pipeline. Scripted Pipeline is written in a limited form of Groovy syntax.

To configure your Pipeline project to use a Jenkinsfile from source control:

##### In SCM
Follow the procedure above for defining your Pipeline through the classic UI until you reach step 5 (accessing the Pipeline section on the Pipeline configuration page).

From the Definition field, choose the Pipeline script from SCM option.

From the SCM field, choose the type of source control system of the repository containing your Jenkinsfile.

Complete the fields specific to your repository’s source control system.
Tip: If you are uncertain of what value to specify for a given field, click its ? icon to the right for more information.

In the Script Path field, specify the location (and name) of your Jenkinsfile. This location is the one that Jenkins checks out/clones the repository containing your Jenkinsfile, which should match that of the repository’s file structure. The default value of this field assumes that your Jenkinsfile is named "Jenkinsfile" and is located at the root of the repository.

Since Pipeline code (i.e. Scripted Pipeline in particular) is written in Groovy-like syntax, if your IDE is not correctly syntax highlighting your Jenkinsfile, try inserting the line #!/usr/bin/env groovy at the top of the Jenkinsfile, [4] [5] which may rectify the issue.

##### Built-in Documentation
The built-in documentation can be found globally at: localhost:8080/pipeline-syntax/.

== Global Variable Reference ==

The variables provided by default in Pipeline are:

*env*
Environment variables accessible from Scripted Pipeline, for example: env.PATH or env.BUILD_ID. Consult the built-in Global Variable Reference for a complete, and up to date, list of environment variables available in Pipeline.

*params*
Exposes all parameters defined for the Pipeline as a read-only Map, for example: params.MY_PARAM_NAME.

*currentBuild*
May be used to discover information about the currently executing Pipeline, with properties such as currentBuild.result, currentBuild.displayName, etc. Consult the built-in Global Variable Reference for a complete, and up to date, list of properties available on currentBuild.
http://10.192.10.45:8080/pipeline-syntax/globals#currentBuild

==> https://jenkins.io/doc/pipeline/steps/
==> https://jenkins.io/doc/pipeline/examples/


### Using a Jenkinsfile

#### Creating a Jenkinsfile
A Jenkinsfile is a text file that contains the definition of a Jenkins Pipeline and is checked into source control.

== Build ==
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
    }
}
"""

== Test ==
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                /* `make check` returns non-zero on test failures,
                * using `true` to allow the Pipeline to continue nonetheless
                */
                sh 'make check || true'
                junit '**/target/*.xml'
            }
        }
    }
}
"""

== Deploy ==
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {
                sh 'make publish'
            }
        }
    }
}
"""


#### Working with your Jenkinsfile

== String interpolation ==
Jenkins Pipeline uses rules identical to Groovy for string interpolation.
"""
def username = 'Jenkins'
echo 'Hello Mr. ${username}'
echo "I said, Hello Mr. ${username}"
"""
>>>
Hello Mr. ${username}
I said, Hello Mr. Jenkins

== Using environment variables ==
Jenkins Pipeline exposes environment variables via the global variable env, which is available from anywhere within a Jenkinsfile.
The full list of environment variables accessible from within Jenkins Pipeline is documented at localhost:8080/pipeline-syntax/globals#env

Referencing or using these environment variables can be accomplished like accessing any key in a Groovy Map, for example:
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}
"""

== Setting environment variables ==
Declarative Pipeline supports an environment directive, whereas users of Scripted Pipeline must use the withEnv step.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    environment {
        CC = 'clang'
    }
    stages {
        stage('Example') {
            environment {
                DEBUG_FLAGS = '-g'
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
"""

"""
Jenkinsfile (Scripted Pipeline)
node {
    /* .. snip .. */
    withEnv(["PATH+MAVEN=${tool 'M3'}/bin"]) {
        sh 'mvn -B verify'
    }
}
"""


== Handling credentials ==

=== Secret text
The following Pipeline code shows an example of how to create a Pipeline using environment variables for secret text credentials.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        // Define agent details here
    }
    environment {
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    }
    stages {
        stage('Example stage 1') {
            steps {
                //
            }
        }
        stage('Example stage 2') {
            steps {
                //
            }
        }
    }
}
"""

=== Secret files


=== SSH User Private Key example
"""
withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'jenkins-ssh-key-for-abc', \
                                             keyFileVariable: 'SSH_KEY_FOR_ABC', \
                                             passphraseVariable: '', \
                                             usernameVariable: '')]) {
  // some block
}
"""


== Handling parameters ==
Configuring parameters with Scripted Pipeline is done with the properties step.

Assuming that a String parameter named "Greeting" has been configuring in the Jenkinsfile, it can access that parameter via ${params.Greeting}:
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    parameters {
        string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
    }
    stages {
        stage('Example') {
            steps {
                echo "${params.Greeting} World!"
            }
        }
    }
}
"""


== Handling failure ==
Declarative Pipeline supports robust failure handling by default via its post section which allows declaring a number of different "post conditions" such as: always, unstable, success, failure, and changed. The Pipeline Syntax section provides more detail on how to use the various post conditions.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'make check'
            }
        }
    }
    post {
        always {
            junit '**/target/*.xml'
        }
        failure {
            mail to: team@example.com, subject: 'The Pipeline failed :('
        }
    }
}
"""

Scripted Pipeline however relies on Groovy’s built-in try/catch/finally semantics for handling failures during execution of the Pipeline.
"""
Jenkinsfile (Scripted Pipeline)
node {
    /* .. snip .. */
    stage('Test') {
        try {
            sh 'make check'
        }
        finally {
            junit '**/target/*.xml'
        }
    }
    /* .. snip .. */
}
"""


== Using multiple agents ==
In the example below, the "Build" stage will be performed on one agent and the built results will be reused on two subsequent agents, labelled "linux" and "windows" respectively, during the "Test" stage.
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                checkout scm
                sh 'make'
                stash includes: '**/target/*.jar', name: 'app'
            }
        }
        stage('Test on Linux') {
            agent {
                label 'linux'
            }
            steps {
                unstash 'app'
                sh 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }
        stage('Test on Windows') {
            agent {
                label 'windows'
            }
            steps {
                unstash 'app'
                bat 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }
    }
}
"""


== Optional step arguments ==
Pipeline follows the Groovy language convention of allowing parentheses to be omitted around method arguments.

statements like the following functionally equivalent:
"""
git url: 'git://example.com/amazing-project.git', branch: 'master'
git([url: 'git://example.com/amazing-project.git', branch: 'master'])
"""

For convenience, when calling steps taking only one parameter (or only one mandatory parameter), the parameter name may be omitted, for example:
"""
sh 'echo hello' /\* short form  \*/
sh([script: 'echo hello'])  /\* long form \*/
"""

#### Advanced Scripted Pipeline

== Parallel execution ==
Refactoring the example above to use the parallel step:
"""
Jenkinsfile (Scripted Pipeline)
stage('Build') {
    /* .. snip .. */
}

stage('Test') {
    parallel linux: {
        node('linux') {
            checkout scm
            try {
                unstash 'app'
                sh 'make check'
            }
            finally {
                junit '**/target/*.xml'
            }
        }
    },
    windows: {
        node('windows') {
            /* .. snip .. */
        }
    }
}
"""


### Branch and Pull Requests
The Multibranch Pipeline project type enables you to implement different Jenkinsfiles for different branches of the same project. In a Multibranch Pipeline project, Jenkins automatically discovers, manages and executes Pipelines for branches which contain a Jenkinsfile in source control.

== Build Triggers ==
'periodically if not otherwise run' 30mins


### Using Docker with Pipeline

#### Customizing the execution environment
Pipeline is designed to easily use Docker images as the execution environment for a single Stage or the entire Pipeline.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        docker { image 'node:7-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
"""

#### Caching data for containers
Pipeline supports adding custom arguments which are passed to Docker, allowing users to specify custom Docker Volumes to mount, which can be used for caching data on the agent between Pipeline runs. The following example will cache ~/.m2 between Pipeline runs utilizing the maven container, thereby avoiding the need to re-download dependencies for subsequent runs of the Pipeline.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        docker {
            image 'maven:3-alpine'
            args '-v $HOME/.m2:/root/.m2'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn -B'
            }
        }
    }
}
"""

#### Using multiple containers
"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker { image 'maven:3-alpine' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker { image 'node:7-alpine' }
            }
            steps {
                sh 'node --version'
            }
        }
    }
}
"""

#### Using a Dockerfile
"""
Dockerfile
FROM node:7-alpine

RUN apk add -U subversion
"""

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}
"""

#### Advanced Usage with Scripted Pipeline

== Running "sidecar" containers ==

== Building containers ==
"""
node {
    checkout scm

    def customImage = docker.build("my-image:${env.BUILD_ID}")

    customImage.inside {
        sh 'make test'
    }
}
"""

"""
node {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.push()
}
"""
"""
node {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.push()

    customImage.push('latest')
}

"""


#### Using a remote Docker server

By default, the Docker Pipeline plugin will communicate with a local Docker daemon, typically accessed through /var/run/docker.sock.

To select a non-default Docker server, such as with Docker Swarm, the withServer() method should be used.

By passing a URI, and optionally the Credentials ID of a Docker Server Certificate Authentication pre-configured in Jenkins, to the method with:
"""
node {
    checkout scm

    docker.withServer('tcp://swarm.example.com:2376', 'swarm-certs') {
        docker.image('mysql:5').withRun('-p 3306:3306') {
            /* do things */
        }
    }
}
"""

#### Using a custom registry
By default the Docker Pipeline integrates assumes the default Docker Registry of Docker Hub.

In order to use a custom Docker Registry, users of Scripted Pipeline can wrap steps with the withRegistry() method, passing in the custom Registry URL, for example:
"""
node {
    checkout scm

    docker.withRegistry('https://registry.example.com') {

        docker.image('my-custom-image').inside {
            sh 'make test'
        }
    }
}
"""


For a Docker Registry which requires authentication, add a "Username/Password" Credentials item from the Jenkins home page and use the Credentials ID as a second argument to withRegistry():
"""
node {
    checkout scm

    docker.withRegistry('https://registry.example.com', 'credentials-id') {

        def customImage = docker.build("my-image:${env.BUILD_ID}")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
"""

### Extending with Shared Libraries
As Pipeline is adopted for more and more projects in an organization, common patterns are likely to emerge. Oftentimes it is useful to share parts of Pipelines between various projects to reduce redundancies and keep code "DRY".

Pipeline has support for creating "Shared Libraries" which can be defined in external source control repositories and loaded into existing Pipelines.


#### Defining Shared Libraries
A Shared Library is defined with a name, a source code retrieval method such as by SCM, and optionally a default version. The name should be a short identifier as it will be used in scripts.

== Directory structure ==
The directory structure of a Shared Library repository is as follows:
"""
(root)
+- src                     # Groovy source files
|   +- org
|       +- foo
|           +- Bar.groovy  # for org.foo.Bar class
+- vars
|   +- foo.groovy          # for global 'foo' variable
|   +- foo.txt             # help for 'foo' variable
+- resources               # resource files (external libraries only)
|   +- org
|       +- foo
|           +- bar.json    # static helper data for org.foo.Bar
...
"""


The *src* directory should look like standard Java source directory structure. This directory is added to the classpath when executing Pipelines.

The *vars* directory hosts scripts that define global variables accessible from Pipeline. The basename of each \*.groovy file should be a Groovy (~ Java) identifier, conventionally camelCased. The matching \*.txt, if present, can contain documentation, processed through the system’s configured markup formatter (so may really be HTML, Markdown, etc., though the txt extension is required).

The Groovy source files in these directories get the same “CPS transformation” as in Scripted Pipeline.

A *resources* directory allows the libraryResource step to be used from an external library to load associated non-Groovy files. Currently this feature is not supported for internal libraries.

Other directories under the root are reserved for future enhancements.


== Global Shared Libraries ==
There are several places where Shared Libraries can be defined, depending on the use-case.
Manage Jenkins » Configure System » Global Pipeline Libraries as many libraries as necessary can be configured.

Since these libraries will be globally usable, any Pipeline in the system can utilize functionality implemented in these libraries.

These libraries are considered "trusted:" they can run any methods in Java, Groovy, Jenkins internal APIs, Jenkins plugins, or third-party libraries. This allows you to define libraries which encapsulate individually unsafe APIs in a higher-level wrapper safe for use from any Pipeline. Beware that anyone able to push commits to this SCM repository could obtain unlimited access to Jenkins. You need the Overall/RunScripts permission to configure these libraries (normally this will be granted to Jenkins administrators).


== Folder-level Shared Libraries ==
Any Folder created can have Shared Libraries associated with it. This mechanism allows scoping of specific libraries to all the Pipelines inside of the folder or subfolder.

Folder-based libraries are not considered "trusted:" they run in the Groovy sandbox just like typical Pipelines.


== Automatic Shared Libraries ==
Other plugins may add ways of defining libraries on the fly. For example, the GitHub Branch Source plugin provides a "GitHub Organization Folder" item which allows a script to use an untrusted library such as github.com/someorg/somerepo without any additional configuration. In this case, the specified GitHub repository would be loaded, from the master branch, using an anonymous checkout.



#### Using libraries
Shared Libraries marked Load implicitly allows Pipelines to immediately use classes or global variables defined by any such libraries. To access other shared libraries, the Jenkinsfile needs to use the @Library annotation, specifying the library’s name:
"""
@Library('my-shared-library') _
/\* Using a version specifier, such as branch, tag, etc \*/
@Library('my-shared-library@1.0') _
/\* Accessing multiple libraries with one statement \*/
@Library(['my-shared-library', 'otherlib@abc1234']) _
"""

The annotation can be anywhere in the script where an annotation is permitted by Groovy. When referring to class libraries (with src/ directories), conventionally the annotation goes on an import statement:
"""
@Library('somelib')
import com.mycorp.pipeline.somelib.UsefulClass
"""

Libraries are resolved and loaded during compilation of the script, before it starts executing. This allows the Groovy compiler to understand the meaning of symbols used in static type checking, and permits them to be used in type declarations in the script, for example:
"""
@Library('somelib')
import com.mycorp.pipeline.somelib.Helper

int useSomeLib(Helper helper) {
    helper.prepare()
    return helper.count()
}

echo useSomeLib(new Helper('some text'))
"""
Global Variables however, are resolved at runtime.


== Loading libraries dynamically ==
"""
library 'my-shared-library'
"""

== Library versions ==
"""
library 'my-shared-library@master'
"""


#### Writing libraries
At the base level, any valid Groovy code is okay for use. Different data structures, utility methods, etc, such as:
"""
// src/org/foo/Point.groovy
package org.foo;

// point in 3D space
class Point {
  float x,y,z;
}
"""

== Accessing steps ==
Library classes cannot directly call steps such as sh or git. They can however implement methods, outside of the scope of an enclosing class, which in turn invoke Pipeline steps, for example:
"""
// src/org/foo/Zot.groovy
package org.foo;

def checkOutFrom(repo) {
  git url: "git@github.com:jenkinsci/${repo}"
}

return this
"""

Which can then be called from a Scripted Pipeline:
"""
def z = new org.foo.Zot()
z.checkOutFrom(repo)
"""


Alternately, a set of steps can be passed explicitly using this to a library class, in a constructor, or just one method:
"""
package org.foo
class Utilities implements Serializable {
  def steps
  Utilities(steps) {this.steps = steps}
  def mvn(args) {
    steps.sh "${steps.tool 'Maven'}/bin/mvn -o ${args}"
  }
}
"""

When saving state on classes, such as above, the class must implement the Serializable interface. This ensures that a Pipeline using the class, as seen in the example below, can properly suspend and resume in Jenkins.
"""
@Library('utils') import org.foo.Utilities
def utils = new Utilities(this)
node {
  utils.mvn 'clean package'
}
"""

If the library needs to access global variables, such as env, those should be explicitly passed into the library classes, or methods, in a similar manner.

Instead of passing numerous variables from the Scripted Pipeline into a library,
"""
package org.foo
class Utilities {
  static def mvn(script, args) {
    script.sh "${script.tool 'Maven'}/bin/mvn -s ${script.env.HOME}/jenkins.xml -o ${args}"
  }
}
"""


== Defining global variables ==
Internally, scripts in the vars directory are instantiated on-demand as singletons. This allows multiple methods to be defined in a single .groovy file for convenience. For example:

"""
vars/log.groovy
def info(message) {
    echo "INFO: ${message}"
}

def warning(message) {
    echo "WARNING: ${message}"
}
"""

"""
Jenkinsfile
@Library('utils') _

log.info 'Starting'
log.warning 'Nothing to do!'
"""


Declarative Pipeline does not allow global variable usage outside of a script directive (JENKINS-42360).
"""
Jenkinsfile
@Library('utils') _

pipeline {
    agent none
    stage ('Example') {
        steps {
             script {
                 log.info 'Starting'
                 log.warning 'Nothing to do!'
             }
        }
    }
}
"""


#### Defining custom steps
Global variables defined in Shared Libraries must be named with all lower-case or "camelCased" in order to be loaded properly by Pipeline. [2]

For example, to define sayHello, the file vars/sayHello.groovy should be created and should implement a call method. The call method allows the global variable to be invoked in a manner similar to a step:
"""
// vars/sayHello.groovy
def call(String name = 'human') {
    // Any valid steps can be called from this code, just like in other
    // Scripted Pipeline
    echo "Hello, ${name}."
}
"""

The Pipeline would then be able to reference and invoke this variable:
"""
sayHello 'Joe'
sayHello() /\* invoke with default arguments \*/
"""

If called with a block, the call method will receive a Closure. The type should be defined explicitly to clarify the intent of the step, for example:
"""
// vars/windows.groovy
def call(Closure body) {
    node('windows') {
        body()
    }
}
"""

The Pipeline can then use this variable like any built-in step which accepts a block:
"""
windows {
    bat "cmd /?"
}
"""


#### Defining a more structured DSL
"""
// vars/buildPlugin.groovy
def call(Map config) {
    node {
        git url: "https://github.com/jenkinsci/${config.name}-plugin.git"
        sh 'mvn install'
        mail to: '...', subject: "${config.name} plugin build", body: '...'
    }
}
"""

Assuming the script has either been loaded as a Global Shared Library or as a Folder-level Shared Library the resulting Jenkinsfile will be dramatically simpler:
"""
Jenkinsfile (Scripted Pipeline)
buildPlugin name: 'git'
"""


#### Using third-party libraries
It is possible to use third-party Java libraries, typically found in Maven Central, from trusted library code using the @Grab annotation. Refer to the Grape documentation for details, but simply put:

"""
@Grab('org.apache.commons:commons-math3:3.4.1')
import org.apache.commons.math3.primes.Primes
void parallelize(int count) {
  if (!Primes.isPrime(count)) {
    error "${count} was not prime"
  }
  // …
}
"""
Third-party libraries are cached by default in ~/.groovy/grapes/ on the Jenkins master.

#### Defining Declarative Pipelines
"""
// vars/evenOrOdd.groovy
def call(int buildNumber) {
  if (buildNumber % 2 == 0) {
    pipeline {
      agent any
      stages {
        stage('Even Stage') {
          steps {
            echo "The build number is even"
          }
        }
      }
    }
  } else {
    pipeline {
      agent any
      stages {
        stage('Odd Stage') {
          steps {
            echo "The build number is odd"
          }
        }
      }
    }
  }
}
"""

"""
// Jenkinsfile
@Library('my-shared-library') _

evenOrOdd(currentBuild.getNumber())
"""

Only entire pipeline`s can be defined in shared libraries as of this time. This can only be done in `vars/\*.groovy, and only in a call method. Only one Declarative Pipeline can be executed in a single build, and if you attempt to execute a second one, your build will fail as a result.


### Pipeline Development Tools

#### Command-line Pipeline Linter
"""
Linting via the CLI with SSH
# ssh (Jenkins CLI)
# JENKINS_SSHD_PORT=[sshd port on master]
# JENKINS_HOSTNAME=[Jenkins master hostname]
ssh -p $JENKINS_SSHD_PORT $JENKINS_HOSTNAME declarative-linter < Jenkinsfile
"""

"""
Linting via HTTP POST using curl
# curl (REST API)
# Assuming "anonymous read access" has been enabled on your Jenkins instance.
# JENKINS_URL=[root URL of Jenkins master]
# JENKINS_CRUMB is needed if your Jenkins master has CRSF protection enabled as it should
JENKINS_CRUMB=`curl "$JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,\":\",//crumb)"`
"""


#### "Replay" Pipeline Runs with Modifications
1. Click on an entry in "Build History"
2. Click on "Replay" in the left menu
3. Modify jenkinsfile as you like
4. Click "Run"

Features
- Can be called multiple times on the same run - allows for easy parallel testing of different changes.
- Can also be called on Pipeline runs that are still in-progress - As long as a Pipeline contained syntactically correct Groovy and was able to start, it can be Replayed.
- Referenced Shared Library code is also modifiable - If a Pipeline run references a Shared Library, the code from the shared library will also be shown and modifiable as part of the Replay page.

#### Pipeline Unit Testing Framework
https://github.com/jenkinsci/JenkinsPipelineUnit
The Pipeline Unit Testing Framework allows you to unit test Pipelines and Shared Libraries before running them in full. It provides a mock execution environment where real Pipeline steps are replaced with mock objects that you can use to check for expected behavior. New and rough around the edges, but promising. The README for that project contains examples and usage instructions.


### Pipeline Syntax

#### Declarative Pipeline
All valid Declarative Pipelines must be enclosed within a pipeline block, for example:

"""
pipeline {
    /* insert Declarative Pipeline here */
}
"""

- *Blocks* must only consist of *Sections*, *Directives*, *Steps*, or assignment statements.
- A property reference statement is treated as no-argument method invocation. So for example, input is treated as input()


== Sections ==
*Sections* in Declarative Pipeline typically contain one or more *Directives* or *Steps*.

==> agent
The agent section specifies where the entire Pipeline, or a specific stage, will execute in the Jenkins environment depending on where the agent section is placed.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'maven:3-alpine' }
    stages {
        stage('Example Build') {
            steps {
                sh 'mvn -B clean verify'
            }
        }
    }
}
"""

==> post
The post section defines one or more additional steps that are run upon the completion of a Pipeline’s or stage’s run (depending on the location of the post section within the Pipeline). post can support one of the following post-condition blocks: always, changed, failure, success, unstable, and aborted. These condition blocks allow the execution of steps within the post section depending on the completion status of the Pipeline or stage.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
    }
}
"""

==> stages
Containing a sequence of one or more stage directives, the stages section is where the bulk of the "work" described by a Pipeline will be located. At a minimum it is recommended that stages contain at least one stage directive for each discrete part of the continuous delivery process, such as Build, Test, and Deploy.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
"""

==> steps
The steps section defines a series of one or more steps to be executed in a given stage directive.


== Directives ==

==> environment
The environment directive specifies a sequence of key-value pairs which will be defined as environment variables for the all steps, or stage-specific steps, depending on where the environment directive is located within the Pipeline.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    environment {
        CC = 'clang'
    }
    stages {
        stage('Example') {
            environment {
                AN_ACCESS_KEY = credentials('my-prefined-secret-text')
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
"""

==> options
The options directive allows configuring Pipeline-specific options from within the Pipeline itself. Pipeline provides a number of these options, such as buildDiscarder, but they may also be provided by plugins, such as timestamps.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
"""

==> parameters
The parameters directive provides a list of parameters which a user should provide when triggering the Pipeline. The values for these user-specified parameters are made available to Pipeline steps via the params object, see the Example for its specific usage.


"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"
            }
        }
    }
}
"""

==> triggers
The triggers directive defines the automated ways in which the Pipeline should be re-triggered. For Pipelines which are integrated with a source such as GitHub or BitBucket, triggers may not be necessary as webhooks-based integration will likely already be present. The triggers currently available are cron, pollSCM and upstream.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    triggers {
        cron('H */4 * * 1-5')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}

"""

==> stage
The stage directive goes in the stages section and should contain a steps section, an optional agent section, or other stage-specific directives. Practically speaking, all of the real work done by a Pipeline will be wrapped in one or more stage directives.

"""

Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
"""

==> tools
A section defining tools to auto-install and put on the PATH. This is ignored if agent none is specified.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    tools {
        maven 'apache-maven-3.0.1'
    }
    stages {
        stage('Example') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}
"""

The tool name must be pre-configured in Jenkins under Manage Jenkins → Global Tool Configuration.

==> input
The input directive on a stage allows you to prompt for input, using the input step. The stage will pause after any options have been applied, and before entering the stage`s `agent or evaluating its when condition. If the input is approved, the stage will then continue. Any parameters provided as part of the input submission will be available in the environment for the rest of the stage.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                }
            }
            steps {
                echo "Hello, ${PERSON}, nice to meet you."
            }
        }
    }
}
"""

==> when
The when directive allows the Pipeline to determine whether the stage should be executed depending on the given condition. The when directive must contain at least one condition. If the when directive contains more than one condition, all the child conditions must return true for the stage to execute. This is the same as if the child conditions were nested in an allOf condition (see the examples below).

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'production'
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
"""

== Parallel ==
Stages in Declarative Pipeline may declare a number of nested stages within them, which will be executed in parallel. Note that a stage must have one and only one of either steps or parallel. The nested stages cannot contain further parallel stages themselves, but otherwise behave the same as any other stage. Any stage containing parallel cannot contain agent or tools, since those are not relevant without steps.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Non-Parallel Stage') {
            steps {
                echo 'This stage will be executed first.'
            }
        }
        stage('Parallel Stage') {
            when {
                branch 'master'
            }
            failFast true
            parallel {
                stage('Branch A') {
                    agent {
                        label "for-branch-a"
                    }
                    steps {
                        echo "On Branch A"
                    }
                }
                stage('Branch B') {
                    agent {
                        label "for-branch-b"
                    }
                    steps {
                        echo "On Branch B"
                    }
                }
            }
        }
    }
}
"""

== Steps ==
Declarative Pipelines may use all the available steps documented in the Pipeline Steps reference, which contains a comprehensive list of steps.

https://jenkins.io/doc/pipeline/steps/

 steps listed below which are only supported in Declarative Pipeline:

==> script
The script step takes a block of Scripted Pipeline and executes that in the Declarative Pipeline.

"""
Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'

                script {
                    def browsers = ['chrome', 'firefox']
                    for (int i = 0; i < browsers.size(); ++i) {
                        echo "Testing the ${browsers[i]} browser"
                    }
                }
            }
        }
    }
}
"""

== Scripted Pipeline ==
if/else
"""
Jenkinsfile (Scripted Pipeline)
node {
    stage('Example') {
        if (env.BRANCH_NAME == 'master') {
            echo 'I only execute on the master branch'
        } else {
            echo 'I execute elsewhere'
        }
    }
}
"""

try/catch/finally
Jenkinsfile (Scripted Pipeline)
"""
node {
    stage('Example') {
        try {
            sh 'exit 1'
        }
        catch (exc) {
            echo 'Something failed, I should sound the klaxons!'
            throw
        }
    }
}
"""



### Scaling Pipelines
One of the main bottlenecks in Pipeline is that it writes transient data to disk FREQUENTLY so that running pipelines can handle an unexpected Jenkins restart or system crash.



## Blue Ocean

## Managing Jenkins
This chapter cover how to manage and configure Jenkins masters and nodes.


## System Administration
This chapter for system administrators of Jenkins servers and nodes. It will cover system maintenance topics including security, monitoring, and backup/restore.


















































































































































































