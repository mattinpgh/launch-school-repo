# Introduction

## A Brief Python History

Python has a rich history that spans several decades. Guido van Rossum began its development in the late 1980s and since then, it has evolved into one of the most popular programming languages.

Guido aimed to create a language that was easy to read, with a clean and intuitive syntax. The name "Python" was inspired by the British comedy group Monty Python's Flying Circus, highlighting Guido's fondness for the show.

Its first public release (version 0.90) was in 1991, with the release of the first production-level version (1.0) in 1994. The language quickly gained popularity due to its simplicity and readability. Since then, new versions have added many new features.

For much of Python's existence, version 2 was the version of choice for many Python programmers. In 2008, the version 3 release made many changes to the language. This version addressed various design flaws and inconsistencies in Python. Since many of these changes were incompatible with version 2, version 3 adoption was slow, mainly limited to new projects and the migration of libraries.

Python 2 support ended in 2020. It no longer receives updates, not even security updates. As of this date, all Python developers should be using Python 3.

## Python's Future

Python's future seems rock solid. Its popularity and continued growth suggest that it will continue to be used widely. Its readability, versatility, and extensive ecosystem suit many applications and problem domains.

It seems unlikely there will be a Python version 4 anytime soon. The creators learned much from the painful, decade-long migration from Python 2 to Python 3 and are not eager to repeat that. Instead, there will be slow, steady improvements to the language with new minor versions (e.g., from 3.9 to 3.10) introduced as needed. More importantly, future changes probably won't introduce significant incompatibilities as did version 3.

## Abstraction

In programming and computer science in general, there is a concept called **abstraction**. Abstraction ensures that users don't need to know what's happening "under the hood." A simple example should help illustrate the concept.

Think about the mobile phone you use daily to communicate with your friends and loved ones. You want to make and receive calls, use text messaging, check your Facebook and X (formerly known as Twitter) accounts, and perhaps take photos. Customers use the manufacturer's user interface (UI) to access the phone's essential features. However, most people don't know or care how to repair their phone or write software for it.

On the other hand, a phone technician needs a different type of interface at a lower level of abstraction. She needs to know how the components work together so she can repair phones that aren't working. Software engineers must understand how the software subsystems interoperate. They must also concern themselves with the Operating System and software development tools. That, too, is at another lower abstraction level.

A similar analysis applies to computers. The user uses computers to listen to music, send emails, play games, and more. They interact with the applications that make these tasks possible without knowing the low-level details.

Programmers, however, operate at a lower level of abstraction by using a programming language like Python. Python, in turn, gets processed by a program called an _interpreter_ ; the interpreter is written in a lower-level language like C. The interpreter converts Python code to a lower-level code format called byte code. Eventually, the original Python code ends up as a series of 1s and 0s that the computer understands. In effect, every programming language requires lower-level layers of code that make it easy to use.

There are also higher-level abstractions. Some Python programmers use the language to design and build tools that operate at a higher level, including libraries and frameworks like NumPy and Flask, which are popular today. These tools let Python developers build programs on top of existing components without knowing how to implement the features they provide.

As a beginner, you must understand how Python, the programming language, and the tools and frameworks you may have heard about are at two different levels of abstraction. It's possible to learn the basics of some of these tools without understanding Python; however, to fully take advantage of their power, you must understand the fundamentals first. Learning Python in depth helps you better understand frameworks, and reading and maintaining programs that use those frameworks becomes easier. Understanding lower levels of abstraction will help you better use tools with higher abstraction levels. This book teaches you Python so that you can recognize and use higher-level abstractions with more granularity.

## Who This Book is For

This book's intended audience is inexperienced or brand-new programmers. If you apply the principles and techniques described here, you'll acquire a solid foundation to build your Python programming career. You may use this knowledge to continue to learn more integrated concepts.

That said, this book goes into sufficient detail that even experienced programmers, including Python programmers, may benefit from reading it. Experienced programmers may find much of the material elementary. However, don't let that stop you from reading the book; you may learn something you didn't know or forgot years ago.

This book guides you through the common pitfalls and time sinks that beginners often experience. It should also provide you with enough practice to commit Python's basic syntax to long-term memory and help you acquire a certain level of **muscle memory** that will help you as a programmer. With this background, you can focus on solving real-world problems and building applications to solve them.

Software development is often perceived as a difficult discipline. It really isn't. Don't get us wrong; it's not easy. However, it does require a particular temperament: patience, persistence, focus, logic, detail-oriented, etc. When a programmer understands and adopts this temperament, their work becomes less frustrating, more fun, and more rewarding.

Perception of a task's difficulty is often inversely proportional to the patience of the person attempting it. Be patient with yourself and willing to take the time to work through the exercises and apply the concepts. You'll soon develop the temperament you need. Before you realize what's happening, you'll find yourself solving problems with code.

A shift in thinking must take place for most people. That will come with practice. Once it happens, your progress will accelerate. That will, in turn, help you develop the ability to think deeply about any programming problem. Most programmers find that being able to think deeply about issues is satisfying, engaging, and a rewarding perk of programming!

## What's Not Covered

While skimming through the contents of this book, you may notice that it doesn't cover many topics that other Python books cover. The omissions are intentional: Python and programming are huge topics, and you'll benefit most from focusing on the fundamentals. Our goal is to introduce you to programming. Python happens to be the vehicle that we are using. As such, it covers the essential information you need to start your journey toward becoming a professional programmer.

Launch School's teaching philosophy centers around [Mastery Based Learning](https://launchschool.com/mastery), which means, among other things, that we introduce students to a new topic only when they have mastered the concepts needed to understand that topic. Learning the basic grammar of a programming language and solving computational problems with that language is a complex skill in its own right. You don't want to spend time learning peripheral information until you have the background and experience to solve programming problems with code.

Let's take a brief look at some of the topics that we chose to omit from this book but which you may find in some other introductory Python material. We cover many of these topics in depth in our Core Curriculum at Launch School, so we don't ignore them. However, there's a time and a place where a novice programmer is ready to learn about some topics.

### 3rd Party Libraries

If you've had any prior exposure to Python, you've probably heard of NumPy, Flask, and other libraries and frameworks. We do not cover any of these in this book.

### Asynchronous Programming

In the wild, Python often has to deal with asynchronous operations, such as requesting and displaying data from a database. However, this advanced feature is best understood when you have a solid grounding in the basics. Initially, you won't have the context to understand why you need asynchronous operations. For that reason, we don't present it in this book.

### Object-Oriented Python

Aside from a brief introduction to Python objects, we'll leave the OOP concepts for the future. You should focus on basic concepts and absorb those concepts before you're ready to tackle OOP. Besides, our [Object Oriented Programming with Python](/books/oo_python) book covers OOP.

### Testing

Testing is crucial to writing good code; however, we don't believe an "introduction to programming" book is the best place to cover it. Testing is a technique you should learn after facing the problems it attempts to solve. It helps to have written sufficiently large programs to grasp that context. We cover testing in our [Core Curriculum](https://launchschool.com/courses).

### Intermediate Language Constructs and Concepts

  * Nested Comprehensions 
  * Dunder Methods 
  * Iterators 
  * Decorators 
  * File I/O 



### Unicode and ASCII

You can think of **Unicode** as a character set that lets computers work with almost any written (non-computer) language. As of 2023, Unicode has nearly half a million characters. Its importance in programming has grown enormously over the last decade or so. However, discussing it any detail piles on a lot of information that really isn't needed by most beginning programmers. Therefore, we will mostly ignore Unicode in this book, though there are a handful of mentions.

Before Unicode, we had the **ASCII character set** , now called the **Standard ASCII character set**. ASCII is now a very small subset of Unicode. It contains 128 characters consisting of:

  * the English letters, both upper- and lowercase (A-Z and a-z) 
  * the 10 Arabic numerals (0-9) 
  * almost 3-dozen control characters like line feeds and carriage returns 
  * almost 3-dozen punctuation characters and symbols 



You can see the standard ASCII character set [here](https://www.ascii-code.com/ASCII).

## How to Read This Book

Reading about programming and writing a program aren't the same things. If you read this entire book but don't write any code, you may understand, intellectually, how to code, but you won't know how to **do it**. If someone asks you to solve a problem with a computer program, you won't be able to complete the task.

There is a "muscle memory" aspect to programming that books and courses often overlook. With the vast amount of information a programmer must remember, practicing some skills until they become automatic is unquestionably crucial. It doesn't require much effort; it happens naturally through repetition and practice. You can learn with your fingers; when you do, you free up your brain to focus on higher-level abstractions.

If you want a real shot at learning how to code, you should do every exercise in this book. Suppose you're going to learn to play a musical instrument. In that case, you must _practice_ your scales on that instrument and develop proficiency. Both are necessary before you can _play_ the instrument well.

Think of the exercises as though you are a musician practicing musical scales and writing a program as playing the instrument. Use the activities to practice and cement the basics into your fingers. The more you practice, the more coding becomes second nature and subconscious, which helps you learn to program.

This book's target audience is the beginner. In computer programming, you must learn an enormous amount of information. It isn't possible to know everything. We recognize that and intentionally avoid topics that aren't beneficial to the beginner. Trust these omissions; we've had some experience with teaching and know how easy it is to get lost "down the rabbit hole" looking for information on unimportant topics. Instead, stay focused. You'll progress at a much faster rate if you do.

That about covers it. Get ready to build the skills you need to become a computer programmer. Don't worry; we're here to coach you along the way. Buckle up and enjoy the ride!

# Preparations

Installing and configuring software can be one of the most challenging tasks a developer performs regularly. Ask a developer what things give him the most trouble, and he will often mention installing and configuring software high on his list. The problem is that computers have different hardware, software (and software versions), and configurations. This adds up to hundreds or thousands of factors that can lead to trouble.

Don't be surprised if you run into trouble in this chapter. If something is going to go wrong, this is where it will do so. Think of it as a learning opportunity -- you can learn a lot by troubleshooting problems.

We recommend using a Macintosh or AWS Cloud9 for our books and courses. While students have enjoyed success with Windows and Linux, they can be trickier to set up. We'll discuss installing Python on all 4 types of systems a little later in this chapter.

Python sometimes gets installed as `python3` and sometimes as `python`. This varies by operating system and version numbers, so predicting which command you should use is difficult. Throughout this book and the Core Curriculum, we assume you can use the `python` command that invokes Python 3. If you can't, or the `python` command runs the wrong version, try `python3` instead. In many cases, either will work.

## The Command Line

Let's start with a brief discussion of the shell command line.

We'll assume you know how to find the command line on your computer and type in commands. When we show example commands or commands that you should type, we will sometimes precede the command with a `$` symbol:
    
    
    $ ls -al
    

The `$` represents the command line prompt, which may differ on your system. That's okay. You aren't meant to type the `$` or any other prompt, so ignore the prompt.

Using the `$` in code blocks interferes with the ability to copy and paste code, so we will try to avoid using it. However, we sometimes need to mix commands and output in the code block. When we do, the `$` is needed to distinguish between code and output. For instance, here's some code mixed with output that requires the `$`:
    
    
    $ which python
    /usr/bin/python
    $ python --version
    Python 3.11.2
    

We usually disable the Copy Code button when displaying code mixed with output and prompts. This causes fewer problems for students that are too quick to copy and paste.

Pay attention to what shell you are using. You can determine the shell with the following command:
    
    
    echo $SHELL
    

If you see output that ends with `/bash`, then you're using the Bash shell. In Bash, the default command line prompt is `$`, which we'll be using as the default prompt.

If, instead of `/bash`, the `echo $SHELL` command outputs something that ends with `/zsh`, then you are using the Zsh shell. In Zsh, the default command line prompt is `%`. We'll show the `%` prompt when showing Zsh-specific commands, but we'll usually use `$` for commands where the shell doesn't matter.

There's a third possibility. If you see a shell name that doesn't end with `/bash` or `/zsh`, then you're using some other shell. Unfortunately, you're on your own if you're using something besides Bash or Zsh. We are unable to support any other shells.

We won't use many shell commands in this book. Most of the commands in this book only show the `python` command. However, you should know how to use the following commands so you can create and manage files and directories:

  * `cd`: navigate between directories 
  * `mkdir`: create (make) a new directory 
  * `rmdir`: delete an empty directory 
  * `touch`: create an empty file 
  * `rm`: delete a file 
  * `git`: so you can push your code to GitHub 



If you need a refresher, please review our [Introduction to the Command Line](/books/command_line) and [Introduction to Git and GitHub](/books/git) books.

## Installing Python

You need Python installed on your computer or cloud environment to get the most from this book. We recommend using Python version 3.10.x or higher if you can. Older versions of Python may suffice, but you could experience issues. For instance, you can't use the `match`/`case` statement with Python versions older than 3.10.0. More recent versions should give you less trouble.

You may already have Python installed. Go to your command line or terminal application and enter the following commands:
    
    
    python3 --version
    python --version
    

If Python is installed, one or both of these commands should print a version number.

If you already have Python installed by your system, it may have restrictive permissions that can impede your ability to install packages, upgrade Python, and perform other development tasks. On a Mac, in particular, you do not want to use the system version of Python; use Homebrew for maximum flexibility.

### When Things Go Wrong

Things don't always go the way you expect. Fortunately, programmers have a time-honored tradition: starting over. No matter how careful you are, things will go wrong one day. A software installation may fail, or a previously working installation suddenly stops working. **When** (not _if_) that happens, starting over may be your best bet.

We'll touch briefly on starting over for each system discussed below.

### Installing Python on a Mac

We recommend using a Macintosh as your best bet for a trouble-free and painless experience. Sadly, that's not a guarantee, but most students have little trouble if they follow the directions in this section and elsewhere.

[Homebrew](https://brew.sh/) is the easiest way to install Python and many Linux tools on a Mac. It lets you install Linux-based programs directly on your Mac without building them from scratch.

If you are using the Apple-supplied Terminal on a Mac that is running one of the Apple processors (e.g., M1, M2, M3, etc.), we recommend making sure the Terminal.app is not set to use Rosetta. To disable Rosetta in the Terminal application, go to Applications, Utilities in the Finder, then right click on the Terminal.app and select the Get Info option. In the General section of the pop up window that appears, make sure "Open using Rosetta" is **not** checked.

If you require Rosetta in the Apple Terminal for some reason, you can use an alternative terminal program like [iTerm2](https://iterm2.com/) instead for your Python programming.

At some point, Apple is likely to remove Rosetta from macOS. If that happens, you won't see the "Open using Rosetta" option in the Get Info window.

Follow the directions at the top of the [Homebrew home page](https://brew.sh/) to install Homebrew.

If running the installation command displays a `Next steps:` part near the end that tells you to run one or more commands, **don't run those commands**. They may interfere with our setup instructions.

Once you've installed Homebrew, restart your Terminal, then run the following command to ensure that Homebrew is correctly installed:
    
    
    brew --version
    

Next, determine what versions of Python you can install with Homebrew:
    
    
    $ brew search python | grep python@
    python@3.10
    python@3.11
    python@3.12
    python@3.7
    python@3.8
    python@3.9
    

The output identifies the different Python versions you can install. Use this list to identify the most recent version. It has the highest number after the first (or only) period (`.`). In this case, version 3.12 is the most recent. You can install this version of Python like so:
    
    
    brew install python@3.12
    

Follow the direction below based on your current shell:

  * **Bash** : Update your [`PATH` environment variable](/books/command_line/read/environmen#patht) as shown here:
    
        WHERE="$HOMEBREW_PREFIX/bin"
    echo "export PATH='$WHERE:$PATH'" >> ~/.bash_profile
    echo "export PATH='$WHERE:$PATH'" >> ~/.bashrc
    echo "alias python=python3" >> ~/.bash_profile
    

  * **Zsh** : Update your [`PATH` environment variable](/books/command_line/read/environment#path) as shown here:
    
        WHERE="$HOMEBREW_PREFIX/bin"
    echo "export PATH='$WHERE:$PATH'" >> ~/.zshrc
    echo "alias python=python3" >> ~/.zshrc
    




Once you've run the above commands, **restart your Terminal application** , then ensure you're using the expected version of Python:
    
    
    python --version
    

You should also be able to use the `python3` command.

**Check Your PATH** with the `echo $PATH` command. You should see something like this:
    
    
    /opt/homebrew/bin:/usr/bin:/usr/sbin:/sbin:/bin
    

On older Macs (those that use an Intel processor), you may see `/usr/local/bin` instead of `/opt/homebrew/bin` at the beginning of the `PATH`:
    
    
    /usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin
    

If you don't see `/opt/homebrew/bin` (or `/usr/local/bin` on an older Mac), at the beginning of that output, you're likely not set up properly (don't worry about the text after the first `:`). Check the following before proceeding:

  * If you're using Bash, you may have a pre-existing `~/.bash_profile` or `~/.profile` file that is interfering with your `~/.bashrc` startup. 
  * If you're using Zsh, you may have a `~/.zshenv`, `~/.zprofile`, or `~/.zlogin` file that is interfering with the startup process of your `~/.zshrc` file. 



If you have one or more of the above files, you may need to edit or remove those files. You should probably seek assistance if you do not know what is happening in those files. You might be better off using AWS Cloud9 instead (see below).

**Starting Over on a Mac**

Starting over on a Mac with Homebrew usually means uninstalling and reinstalling Python. You may also have to reinstall any Python packages you had installed previously.

Sometimes, you may have to take that one step further and uninstall Homebrew entirely, then reinstall it. You can find the uninstall directions on the Homebrew site. As of this writing, those directions are [here](https://mac.install.guide/homebrew/5.html).

In the worst case, starting over may mean restoring from a reliable backup, such as Time Machine. This lets you return your system to a time when the system was working. This is a drastic solution, but you'll be thankful you had those backups. You do have backups, don't you?

### Installing Python on GitHub Codespaces

If you don't have a Macintosh or don't want to use your Mac as a development environment, you can try using [GitHub Codespaces](https://github.com/features/codespaces) instead. GitHub Codespaces is a low-cost, cloud-based alternative to using your own system for development. They also have free environments which can be sufficient for Launch School, provided you take care not to exceed the free limits:

  * Use the smallest (2-core with 8GB RAM and 32GB disk space) codespaces 
  * Don't leave codespaces running. 
  * Don't create multiple codespaces. 
  * Don't add additional disk space. 



Even if you exceed one or more of these limitations, your monthly charge is typically less than a few US dollars.

To use GitHub Codespaces, you only need a modern web browser and an internet connection. Codespaces is also relatively trouble-free. However, GitHub may change its UI and software more often than Apple changes macOS, which can lead to outdated instructions. We do our best to update our instructions when needed.

By default, codespaces have an older version of Python installed, with no obvious way to upgrade to a more recent version. For instance, as of this writing, GitHub Codespaces have Python 3.10 pre-installed. For now, we're not going to worry about this. Use whatever version is already installed. You can determine that version by running the following command:
    
    
    python --version
    

We discuss how you can install more recent versions of Python in the Core Curriculum.

**Starting Over on GitHub Codespaces**

Starting over On GitHub Codespaces usually means creating a new "Blank" template. You can then copy over any files you want to save from the old workspace to the new one. Finally, remove the old workspace to avoid GitHub charges. You may need to reinstall any programs you installed in the old workspace.

### Installing Python on AWS Cloud9

If you don't have a Macintosh or don't want to use your Mac as a development environment, you can try the [AWS Cloud9](https://aws.amazon.com/cloud9/) service. Cloud9 is a low-cost, cloud-based alternative to using your own system for development. You can get up to a year of free service, provided you take care not to exceed the free tier limits:

  * Don't leave workspaces running. 
  * Don't create multiple workspaces. 
  * Don't add additional disk space. 



Even if you exceed one or more of these limitations, your monthly charge is typically less than a cup of plain black coffee from a vending machine.

To use Cloud9, you only need a modern web browser and an internet connection. Cloud9 is also relatively trouble-free. However, AWS changes its UI and software more often than Apple changes macOS, which can lead to outdated instructions. We do our best to update our instructions when needed.

By default, Cloud9 workspaces have an older version of Python installed, with no obvious way to upgrade to a more recent version. For instance, as of this writing, Cloud9 workspaces with Amazon Linux 2023 have Python 3.9 pre-installed. For now, we're not going to worry about this. Use whatever version is already installed. You can determine that version by running the following command:
    
    
    python --version
    

We discuss how you can install more recent versions of Python in the Core Curriculum.

**Starting Over on Cloud9**

Starting over On AWS Cloud9 usually means creating a new workspace with your desired platform choice. You can then copy over any files you want to save from the old workspace to the new one. Finally, remove the old workspace to avoid AWS charges. You may need to reinstall any programs you installed in the old workspace.

### Installing Python on Other Linux Systems

Most Linux systems come with Python pre-installed. However, it is often an older version. For now, don't worry about this. You should use the version that is already installed in your workspace. You can determine that version by running the following command:
    
    
    python --version
    

Refer to the [official Python installation instructions](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) if you need to install Python on your system. However, we are unable to provide any support for this process.

**Starting Over on Linux**

Starting over on Linux systems often begins with uninstalling and reinstalling Python. If that works, you're golden and can get back to work.

If that doesn't work, you may need to restore from a reliable backup. This lets you return your system to a time when the system was working. This is a drastic solution, but you'll be thankful you had those backups. You do have backups, don't you?

### Installing Python on Windows

We do not recommend using Windows and cannot provide support for it. However, many Launch School students have successfully used the [Windows Subsystem for Linux Version 2](https://learn.microsoft.com/en-us/windows/wsl/about) in our courses. WSL2 essentially lets Windows users work with Linux on a Windows system. See the previous section for further information.

**Starting Over on Windows**

Starting over on Windows often begins with uninstalling and reinstalling Python. If that works, you're golden and can get back to work.

If you're using WSL2, you may be able to delete your development environment and then recreate it. You'll need to reinstall any programs you need, but that's better than restoring your entire Windows system.

If that doesn't work, you may need to restore from a reliable backup. This lets you return your system to a time when the system was working. This is a drastic solution, but you'll be thankful you had those backups. You do have backups, don't you?

## Using a Code Editor

Developers often use a code editor to write code. A code editor creates plain text documents with no styling or formatting. If you already have a favorite code editor (e.g., Visual Studio Code, Vim, Emacs, etc.), use it to work through this book.

If you do not have a preferred code editor, we strongly recommend using [Visual Studio Code](https://code.visualstudio.com/) (also known as VSCode). It's free and built as an open-source project. It's highly polished and pleasant to look at and use. Most surprisingly, perhaps, is that it comes from Microsoft. Its popularity is skyrocketing in the developer community.

VSCode comes in Mac, Windows, and Linux versions.

Do not use a word processor when writing code. Word processors are for writing, not coding. They often inject invisible characters or whitespace into the document to help format and style it. While that can make your prose look great, it doesn't work well with code. Code written with a word processor may not run even if you copy and paste it into a code editor before saving it.

## Python Documentation

As you start your journey as a developer, you must learn how to read **documentation**. Like all popular programming languages, Python comes with a rich set of standard libraries you can use. However, you must study the Python documentation to familiarize yourself with the language and its different classes, modules, functions, and methods.

Some developers also refer to the documentation for a class, module, function, or method as its **API**. API is a somewhat overloaded acronym for Application Programming Interface that can refer to the documentation or how applications talk to each other. If someone asks whether you looked at the `list` API, they want to know if you read the Python documentation for the `list` class. However, if they want to know how to use Google's Search API, they want you to tell them how those search services can be used programmatically.

In this section, we'll look briefly at the Python documentation. Since the documentation sometimes changes structure and appearance, this quick look doesn't use images or many details of the documentation's organization.

The [Python docs website](https://www.python.org/doc/), as of August 2023, has a button near the top labeled "Python Docs." This button takes you to the most recent version of the documentation, which may not be the same as your Python version. If the version number matters, view the Documentation Releases by Version.

The main page for each documentation version should show a high-level table of contents. However, finding the information you need may not be painless even with that table of contents. For the purposes of this book, you can focus on these parts:

  * The [Language Reference](https://docs.python.org/3/reference/index.html) explores the language itself. Oddly, the most useful sections for beginners are near the bottom of the page (as of December 2023): 
    * **Expressions**
    * **Simple Statements**
    * **Compound Statements**
  * The [Library Reference](https://docs.python.org/3/library/index.html) covers all built-in classes and modules. The most valuable sections (as of December 2023) are: 
    * **Built-in Types**
    * **Built-in Functions**
    * **Built-in Constants**
  * Turn to the [Glossary](https://docs.python.org/3/glossary.html) if you need unfamiliar terms explained. 
  * You can use the [Complete Table of Contents](https://docs.python.org/3/contents.html) if you know the right words. Your browser's in-window search will help you quickly find the appropriate entry. 



We'll refer you to the documentation to highlight special items of interest when the information will benefit you most. For now, bookmark the documentation and try to familiarize yourself with its structure.

It's worth noting that the documentation is not always helpful, even when you find the right page. You can search the web for a better explanation if necessary. Be careful, though: searches often turn up outdated or incorrect content, so focus on recent items and try to look at several pages for conflicting information. AI tools like ChatGPT may also be helpful, but be extra careful: **AI tools may lie to you. Convincingly**.

# Using Python

In this chapter, we'll show you how to run Python code. We'll also describe some basic Python coding conventions and briefly discuss Python packages. Finally, we'll look at a basic debugging technique. None of this information is exhaustive, but it should help you get through the rest of the book.

There are two main ways to run Python code with the `python` command:

  * You can use a special line-by-line execution mode of `python` to execute code one line at a time. This mode is most helpful in determining what built-in functions and methods will do under different circumstances. 
  * You can use the `python` command to run the code from a file on your disk. This is the most common way to run Python code. 



Note that we will be showing you some Python code in this chapter without thoroughly explaining what the code does. What's important in this chapter is learning how to use Python, whether it's using a REPL or running a Python program from a file. We'll also briefly talk about indentation, continuations, and using the `print` function.

## Indentation

Before we begin doing anything with Python -- even running some trivial code -- we need to talk about indentation. Python is unusual among programming languages; it uses indentation to understand your code.

Most programming languages have little care about indentation. While most programmers indent their code carefully, this choice primarily concerns readability. Simple carelessness, though, often leads to code that is inconsistently or improperly indented. However, the language interpreter or compiler doesn't care about indentation. The code still works, no matter how it's indented. For instance, in the JavaScript language, you'll encounter code like this:
    
    
    function doubleArray(array) {
      // some code here
      for (let index = 0; index < array.length; index += 1) {
        // some more code here
        array[index] = 2 * array[index];
      }
    }
    

Everything is neatly indented to show the structure of the code. The main program is flush against the left margin, the function body is indented by two spaces, and the body of the `for` loop is indented by another two spaces. However, JavaScript doesn't care. The following code is equally valid but less readable:
    
    
    function doubleArray(array) {
    // some code here
    for (let index = 0; index < array.length; index += 1) {
    // some more code here
    array[index] = 2 * array[index];
    }
    }
    

This code is also perfectly acceptable to JavaScript:
    
    
              function doubleArray(array) {
    // some code here
       for (let index = 0; index < array.length; index += 1) {
                                    // some more code here
                          array[index] = 2 * array[index];
                 }
       }
    

Python is different. The code **must** be indented and indented consistently in any given "block" of code. For instance, the Python equivalent of the above code looks like this:
    
    
    def double_list(input_list):
        # some code here
        for index, element in enumerate(input_list):
            # some more code here
            input_list[index] = 2 * element
    

The function definition (`def`) is flush left. The function's body is indented by 4 spaces, and the body of the `for` loop is indented another 4 spaces. If you try to rewrite that code without the indentation, Python will raise an error:
    
    
    def double_list(input_list):
    # some code here
    for index, element in enumerate(input_list):
        # some more code here
        input_list[index] = 2 * element
    # IndentationError: expected an indented block after
    # function definition on line 1
    

Another thing to note: most languages delineate the beginning and end of the code inside multi-line statements like function definitions and loops. JavaScript and many other languages use the `{` and `}` characters to mark a block's beginning and end. Other languages use keywords like `do` and `end` to do the same thing. Python doesn't do this. Okay, it does use a `:` to mark the beginning of a block of code, but the block ends only when the indentation is reduced:
    
    
    def double_list(input_list):
        for index, element in enumerate(input_list):
            input_list[index] = element
    
        return input_list
    

In this code, the `return` statement is not part of the `for` loop since its indentation is less than that of the loop's body. The indentation marks the beginning and end of the body of a multi-line statement.

If you've programmed in other languages, using indentation in Python may initially seem quirky. However, once you get used to it, you'll wonder why other languages do it differently.

Okay, let's learn how to use Python with these preliminaries out of the way.

## Using the REPL

Let's first discuss how to execute Python code line-by-line. We'll use Python's built-in **REPL** (_Read-Eval-Print Loop_). The REPL is an interactive environment where you type Python statements and expressions. You will see the results immediately. Python has a built-in REPL that's ideal for beginners exploring the language.

REPLs are programs that let you write and execute small snippets of code interactively. You can use Python's REPL to quickly try code to see what happens.

Python has several REPLs, but the most basic is the built-in REPL. The `python` command invokes the built-in REPL when run without arguments. For instance:
    
    
    $ python
    Python 3.11.2
    Type "help", "copyright", "credits" or "license" for more
    information.
    >>>
    

The last line (`>>>`) is the REPL's prompt. You can enter a Python statement or expression after the prompt and see its output or return value, if any, below the prompt. It also distinguishes between what you type and the resulting output. You can enter as much Python code as you want, one at a time. Each time you enter a complete statement or expression, Python executes it and displays any output or return values produced.

As with shell commands that produce output, we disable the Copy Code functionality when depicting REPL sessions.

The REPL's prompt may vary depending on your system configuration, so it may look different on your computer. That's okay. Just ignore the leading `>>>` when it appears in a code block. Do not type it. For example, in the following, you will type `print('hello world!')` at the `>>>` prompt, then press the Return or Enter key. The REPL will then display the output produced by `print(...)` (`hello world!`) followed by a new `>>>` prompt.
    
    
    >>> print('hello world!')
    hello world!
    >>>
    

You don't have to use `print` explicitly if it's the last line entered. The REPL outputs the evaluated value of the last line of code to execute. In fact, this is a great way to perform quick mathematical calculations:
    
    
    >>> 4 * 9 + 6
    42
    >>>
    

Multi-line statements, such as `if` statements, can be tricky since you must remember to indent code properly and use colons (`:`) where required. You also need to press the Return or Enter key once more to show that you are done typing. It looks like this:
    
    
    >>> a = 42    # This is assignment; we'll discuss it later
    >>> if a > 42:
    ...     print('No')
    ... else:
    ...     print('Yes')
    ...
    Yes
    >>>
    

Remember: indentation is **important** in Python.

Notice that the continuation lines in multi-line statements use `...` as a prompt. As with `>>>`, the actual prompt may vary. You do not type the prompt, no matter what the prompt looks like.

You can also define and call functions in the REPL:
    
    
    >>> def add_three(value):
    ...     return value + 3
    ...
    >>> add_three(39)
    42
    

### The help Function

The `help` function lets you request help in the Python REPL:

  * Display a short summary of how to use `help`:
    
        help()
    

Type `q` and press {Return} to exit `help`.

  * Display a short summary of how to use the `len` function:
    
        help(len)
    

  * Display a summary of the `str` class:
    
        help(str)
    

  * Display a summary of the `bool` class by passing `help` a Boolean value:
    
        help(3 == 4)
    




`help` is very flexible and will try to give you helpful information, no matter what value you pass it. You can't always predict how it might interpret some input, but it's reasonably good at guessing your intent.

### Additional REPL Tips

To exit the REPL, type `exit()` or `quit()` followed by the Return or Enter key. Press the Control-D keyboard combination for an even easier way to close the REPL.

As of Python 3.13.0, you only have to type `exit` or `quit`; you may omit the parentheses.

Use the Up and Down arrow keys to navigate through your REPL history. You can use the Left and Right arrow keys to position the cursor and begin editing some prior input. (This may not work if your Python was built without the proper "readline" support.)

The REPL is a great way to experiment and learn with Python. You can quickly test out ideas, understand how functions behave, or even debug code snippets without the overhead of creating a full-fledged script.

#### Copying and Pasting in the Python REPL

Copying and pasting code into the Python REPL isn't reliable. In particular, if all 3 of the following statements are true, pasting into the REPL probably won't work:

  * At least one line of code is indented. 
  * One of the indented lines is followed by one or more empty lines. 
  * The line after the empty line(s) is indented less than the original indented line or not indented at all. 



You will probably get an indentation error on the line after the empty lines.

Unfortunately, there is no way to fix the copy and paste issue in Python prior to 3.13.0. However, there are at at least two workarounds:

  * Use [Coderpad](https://coderpad.io). You can paste code into the REPL side of the Coderpad workspace (the right side) and it will work properly. You can also paste into the left side of the workspace, but you'll have to click the Run button. Coderpad is a good choice since we use it for assessments. However, there are some limitations with Coderpad, such as not being able to install packages. 
  * Use Jupyter Notebook or JupyterLab. Just paste your code into a notebook, then run it. (We'll discuss these two products a bit later.) 



Python 3.13.0 introduced a new feature in the REPL that makes pasting code work more reliably. To paste code cleanly in the REPL, first press the `{F3}` key. This should change the prompt to `(paste)`. You can now paste your code. When you are done pressing, press the `{F3}` key again. You may need to press `{Return}` to get back to the `>>>` prompt.

## Running Python Code From a File

Suppose you have a file named `example.py` that contains some Python code you want to execute. For instance, assume the file contains the following code:
    
    
    print('I wish to complain about this parrot.')
    print("It's probably pining for the fjords!")
    

Once you've saved this file, you can run it as follows:
    
    
    $ python example.py
    I wish to complain about this parrot.
    It's probably pining for the fjords!
    

Note that files with Python code typically have a `.py` extension.

When you run a Python file from the command line, the Python **compiler** reads and converts the code into a form the computer understands. The compiled code is called **byte code**. Once the byte code is available, it gets passed to the **interpreter** , which executes the code. You don't need to know much about the compiler and interpreter except that you should recognize the terms.

One last tip: some Python programs may run for a long time, maybe infinitely. That may be intentional or due to a logic error. Regardless, you can use the Control-C keyboard combination to terminate such programs. Control-C sends an interrupt signal to the running program, which usually ends the program. For instance, try running the program in this `endless_loop.py` file:
    
    
    import time
    
    while True:
        time.sleep(1)
        print(time.asctime())
    

Press the Control-C keyboard combination when you tire of watching the endless output.

## Stylish Python

The Python community has developed stylistic conventions that help make Python code easier to read and write. There are actually multiple conventions, and the different guidelines sometimes disagree. However, there's plenty of overlap in the recommendations.

Adhering to the style conventions of a programming language is helpful and meaningful even when you disagree with some recommendations. You probably won't be the sole person developing and maintaining a software project; sticking to a particular style convention helps your teammates and future maintainers understand your code. It's hard enough to understand code written by someone else; don't make it more challenging with unusual or non-standard stylistic choices.

The conventions discussed in this section are specific to the Python community. Other programming languages -- and even some Python sub-communities -- may have different preferences about each guideline.

Here's a short list of guidelines that we recommend. If you already work with a formal set of guidelines, please feel free to use them. If you don't, our suggestions should help you write readable code.

  * Set your text editor to use four space characters -- **not tabs** \-- for indentation.

  * Set your text editor to expand tab characters to spaces.

  * Limit code lines and comments to 79 characters. This guideline isn't universal, but it helps readability. Not all developers have massive screens or good eyesight, so be kind and stick to this guideline.

  * Use spaces around operators, except for `**`, which should not be surrounded by spaces:
    
        print(3 + 4)    # + is an operator
    print(5 * 7)    # * is an operator
    print(6 - 2)    # - is an operator
    print(7 / 3)    # / is an operator
    print(8**3)     # ** operator is not surrounded by spaces
    my_num = 3      # = is an operator
    
    
        print(3+4)
    print(5* 7)
    print(6 -2)
    print(7/3)
    print(8 ** 3)   # Don't use spaces with **
    my_num=3
    

  * Python uses the `#` character as the beginning of a comment. Comments run through the end of the line.
    
        # This line only has a comment
    ultimate_answer = 42        # initializing variable
    a_round_number = 3.141592   # another initialization
    

Programmers use comments to leave notes for other programmers or themselves at a later point in time. However, don't overdo your comments. Let your code do the talking instead.

  * Some Python language features use **code blocks** \-- one or more lines of code that are treated as a unit. The statement introducing a block of code ends with a `:`. In contrast, the block is indented with 4 spaces. The block ends when you outdent back to the original level.
    
        if is_ok():
        print('first thing')
        print('another thing')
        print('yet another thing')
    print('This is not part of the above block')
    
    if is_something():
        print('do something')
        print('do another thing')
    else:
        print('do something else')
    
    while try_again():
        print('first thing')
        print('another thing')
        print('yet another thing')
    print('The loop has ended.')
    

You can also have multiple levels of indentation, though you should avoid using more than two levels:
    
        if value <= 10:
        print('value <= 10')
        if value >= 5:
            print('value >= 5')
        else:
            print('value < 5')
    else:
        print('value > 10')
    

  * Use spaces between operators and operands to make your code less cluttered and easier to read:
    
        sum=x+5              # bad
    sum = x + 5          # good
    




## PEPs

The previous section covers the essential style conventions you need to get started. If you want more information about Python styling, we recommend the [Style Guide for Python Code](https://peps.python.org/pep-0008/), otherwise known as **PEP 8**. Check it out, but don't try to memorize all of the rules right away.

PEP stands for Python Enhancement Proposal. PEPs are numbered design documents that provide information and recommendations to the Python community, information about new or proposed language features, and standards and conventions.

PEP 8 is perhaps the best-known and most widely used PEP. It is the basis for most Python style conventions and should be reviewed occasionally by Python developers.

## Continuation Lines

If you checked out PEP8, you may have noticed that one of the stylistic conventions in Python is that code lines should be no more than 79 characters in length. That means that you need to learn how to continue code over multiple lines. This can get a little tricky, but there are several ways to continue code over multiple lines:

  * String literals can be continued over several lines, provided you enclose all the string content in a set of parentheses:
    
        return ("This is a long string. "
            "It's actually very long. "
            "It spans multiple lines. "
            "Are you getting tired of this? "
            "So am I.")
    

This also works with f-strings and r-strings, which we'll encounter later.

Sometimes, a triple quoted string is easier to deal with:
    
        return """
        This is a long string.
        It's actually very long.
        It spans multiple lines.
        Are you getting tired of this?
        So am I.
    """
    

It's worth noting that triple-quoted strings preserve leading whitespace and any newline characters. You also don't need parentheses.

  * Multi-value literals, such as lists and tuples, can be written over several lines by just using line-breaks between the brackets, braces, or parentheses used by the literal:
    
        my_list = [
        "Antonina",
        "Brandi",
        "Trevor",
    ]
    
    
        my_tuple = (
        3.141592,
        2.718282,
        1.414213,
    )
    
    
        my_set = {
        "Dog",
        "Cat",
        "Pet",
    }
    

When writing collection literals over multiple lines like this, the convention is to end every item in the list with a comma, including the last element. This convention makes it easy to add new elements to the end of the collection, and also permits easy sorting and rearranging.

  * You can use parentheses to delimit code that will be split over multiple lines:
    
        return (obj.bar1
          + obj.bar2
          + obj.bar3)
    

  * You can use a backslash to end any line you want to continue:
    
        result = value1 + \
             value2 + \
             value3
    

A good rule of thumb is that you can use a backslash wherever you can put a space.

That said, you should use backslash continuations sparingly, and only where they improve readability. You should not use backslashes when they aren't syntactically required for continuation. It's usually better to use one of the other continuation techniques.




The trickiest part of using continuations is often how to indent the continuation lines, especially when using `if` and `while` statements and comprehensions. The only rule we can offer is to aim for readability and consistency. The continued code should clearly be connected to the first line, and shouldn't blend into any following code blocks. We'll show some readable examples in this book and the Core curriculum.

## Using JupyterLab/Jupyter Notebook

[JupyterLab and Jupyter Notebook](https://jupyter.org/) are alternatives to the standard Python REPL. Both can also operate as a complete Python program editor and documentation generator. Jupyter offers many advantages over using the built-in REPL. The most significant benefits may be that you can write and try it out, copy and paste code from Launch School materials and elsewhere, and much more. The copy-and-paste functionality is especially handy as the built-in Python REPL badly mishandles blank lines in indented code when pasting. The built-in REPL is effectively unusable when you want to copy and paste code that has blank lines in indented code.

The easiest way to use Jupyter is to use one of the experimental browser-based versions of JupyterLab and Jupyter Notebook at the [Try Jupyter page](https://jupyter.org/try). You don't have to install anything -- not even Python. All you need is your browser. However, you won't have any control over what version of Python you are using. To see what version of Python is currently being used by one of these experimental programs, run the following code in a notebook:
    
    
    import platform
    platform.python_version()
    

If you would rather install your own version of Jupyter, you can do so on Macs, Windows (WSL2 preferred), and most Linux systems. Note that we don't recommend installing Jupyter on AWS Cloud9; the process is currently too complicated. It doesn't play well with Cloud9's "Preview" browser.

Recent versions of Linux Operating Systems (including the WSL2 version of Ubuntu) are starting to implement a security measure that prevents installing packages on top of a system-controlled version of Python. That means that installing Jupyter will fail on these systems. Later, in PY101, we'll show you how to set up a virtual environment that will let you install Jupyter on these systems. You can skip the rest of this section unless you are using a Macintosh with Homebrew.

On Mac systems, you can easily install JupyterLab with Homebrew:
    
    
    brew install jupyterlab
    

Once installed, you can start Jupyter with one of these commands:
    
    
    jupyter lab
    jupyter notebook
    

The program will open in your browser, after which you can create a new notebook and write some code. When you want to execute the code, press {Shift}{Enter}.

Please note that we cannot support using, configuring, and troubleshooting JupyterLab and Jupyter Notebook. However, both products are widely used in the Python community. Help should be widely available, starting with the [Jupyter website](https://docs.jupyter.org/) and the [Jupyter community forums](https://discourse.jupyter.org/).

## Debugging Python Code with print

Python has a nifty built-in module called Pdb that lets you step through programs to see what happens on each line of code. This is a fantastic way to debug programs. However, before using Pdb to debug a program, you must learn how to use it. Now isn't the time to do that. We'll learn how to use Pdb later in the Core Curriculum.

For now, the easiest way to debug Python programs is to add `print` statements at strategic points in your program. These `print` statements can help quickly identify where and why your program isn't working.

Suppose we are writing a program that displays the maximum numeric value from a list of numeric strings:
    
    
    max = '0'
    for number in ['10', '2', '34', '6', '25']:
        if number > max:
            max = number
    
    print('max value is', max)
    

Some of you may already see the problem, but not everyone will. Let's walk through using `print` to debug this code.

First, let's run the code:
    
    
    $ python compute_max.py
    max value is 6
    

This answer isn't correct - the maximum numeric value should be `34`, not `6`. Let's use `print` to try to diagnose the problem. There are two crucial values we need to see what is happening, `max` and `number`, so we'll print both values during each iteration of the loop:
    
    
    max = '0'
    for number in ['10', '2', '34', '6', '25']:
        # highlight
        print('max =', max, 'number =', number)
        # endhighlight
        if number > max:
            max = number
    
    print('max value is', max)
    
    
    
    $ python compute_max.py
    max = 0 number = 10
    max = 10 number = 2
    max = 2 number = 34
    max = 34 number = 6
    max = 6 number = 25
    max value is 6
    

This output shows that `max` was `0` and `number` was `10` on the first iteration. (Remember, though, that these values are strings.) On the second iteration, `max` was `10` and `number` was `2`. This seems reasonable: `10 > 0`, so `max` gets set to `10`. However, on the 3rd iteration, we see that `max` is `2`. That can't be right: `2 < 10`, so `max` should still be equal to `10`.

Let's display the value of `number > max` to get a better idea of what's happening:
    
    
    max = '0'
    for number in ['10', '2', '34', '6', '25']:
        # highlight
        print('max =', max, 'number =', number,
              'number > max =', number > max)
        # endhighlight
        if number > max:
            max = number
    
    print('max value is', max)
    
    
    
    $ python compute_max.py
    max = 0 number = 10 number > max = True
    max = 10 number = 2 number > max = True
    max = 2 number = 34 number > max = True
    max = 34 number = 6 number > max = True
    max = 6 number = 25 number > max = False
    max value is 6
    

Hmm. It looks like the comparison is always `True` except when we check `6` against `25`. This is a huge clue. It tells us we're comparing `number` and `max` as strings, not numbers. **Strings are compared lexicographically, e.g., character by character** , so `'25' < '6'` while `'6' > '34'`. That's because `'2' < '6'` and `'6' > '3'`. To fix this program, we must compare the values numerically. We can do this by converting the strings to integers when comparing them.
    
    
    max = '0'
    for number in ['10', '2', '34', '6', '25']:
        print('max =', max, 'number =', number,
              'number > max =', number > max)
        # highlight
        if int(number) > int(max):
        # endhighlight
            max = number
    
    print('max value is', max)
    
    
    
    $ python compute_max.py
    max = 0 number = 10 number > max = True
    max = 10 number = 2 number > max = True
    max = 10 number = 34 number > max = True
    max = 34 number = 6 number > max = True
    max = 34 number = 25 number > max = False
    max value is 34
    

Now we're getting the correct answer: `34` is the largest numeric value in the list.

Before we leave this problem, let's go ahead and delete the debugging code (the `print` statement) and run the program one last time:
    
    
    max = '0'
    for number in ['10', '2', '34', '6', '25']:
        # print statement deleted
        if int(number) > int(max):
            max = number
    
    print('max value is', max)
    
    
    
    $ python compute_max.py
    max value is 34
    

It's worth your time to learn to use this debugging technique. In particular, you may need it in Coderpad, which we use for interview assessments. Coderpad does not support debugging tools, so `print` is the only way to go.

## About the Exercises

A question that comes up often with our exercises is "My answer is different from Launch School's, but it still works. What should I do?"

Even with simple problems, there are often several different ways to solve an exercise, and sometimes many different ways. At this stage in your journey, the important part is to understand what you’ve read and be able to use that knowledge to answer questions, even if your answer is a little different. Once you're satisfied with your answer, you want to check it against Launch School's answer. Your answer doesn't have to be the same as ours. In fact, having an alternative answer affords you the opportunity to learn from seeing a different approach. How is your solution different from Launch School's? Do you understand our solution too?

Of course, you should be sure to check that your answer satisfies the requirements of the exercise. Does the output match the expected output, exactly? Does it properly handle any edge cases that may be mentioned? Sometimes, an answer may seem like it's correct, but you may have missed one of the requirements.

As long as you understand both your solution and ours, feel free to move on to the next exercise. At this point, you’re building up an awareness of the language, functions, methods, and all the different ways you can do things. Having a different answer is not bad or a sign that you need to go back.

##  Exercises

  1. Create a directory named `my_folder` and navigate to that directory. Create two files named `one.py` and `two.py` in `my_folder`. Add the following Python code to `one.py`:
    
        print('This is file one')
    

Write a similar program in `two.py` that prints `This is file two`.

When finished, run both programs with the `python` command.

#### Solution
    
        $ mkdir my_folder
    $ cd my_folder
    $ touch one.py
    $ touch two.py
    
    # Use your editor to edit one.py and two.py
    
    $ python one.py
    This is file one
    
    $ python two.py
    This is file two
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. When you finish Exercise 1, navigate to the directory above the `my_folder` directory and delete all the content you generated in Exercise 1 with one command.

**WARNING** : The `rm` command is **DANGEROUS**. You can't undo this command. The effects are permanent. Ensure you are in the correct directory and are using the right name of the directory you want to delete. **Check three times!**

#### Solution
    
        $ cd ..
    $ pwd   # Use to check where you are
    $ ls    # Use to verify my_folder exists
    $ rm -R my_folder
    

To repeat, **use extreme caution** when using the `rm` command. It's destructive and irreversibly deletes folders and files. That's why we use `pwd` and `ls` to ensure what we're about to do is being done where it should be done.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Data Types

A core job of most programming languages is dealing with data. Everything you do in a computer program involves data in some way. Data in any programming language has different data types. Data types help programmers and their programs determine what they can and cannot do with a given piece of data. This chapter takes a quick tour of Python's basic data types. **Everything you do in Python involves data and data types.**

Everything with a value in Python is said to be an **object**. Furthermore, each object has an associated **data type** or, more concisely, **type** , which has an associated **class**. For instance, the objects `42` and `123` are instances of the integer type, i.e., the `int` class. Similarly, the values `True` and `False` are instances of the Boolean type, i.e., the `bool` class.

In Python, the terms _object_ and _value_ can be used interchangeably, as can the terms _class_ , _data type_ , and _type_. We will use them that way, too.

## Data Types

Python has a large number of built-in data types compared to many other languages:

Data Type | Class | Category | Kind | Mutable  
---|---|---|---|---  
integers | `int` | numerics | Primitive | No  
floats | `float` | numerics | Primitive | No  
boolean | `bool` | booleans | Primitive | No  
strings | `str` | text sequences | Primitive | No  
|  |  |  |   
ranges | `range` | sequences | Non-primitive | No  
tuples | `tuple` | sequences | Non-primitive | No  
lists | `list` | sequences | Non-primitive | **Yes**  
dictionaries | `dict` | mappings | Non-primitive | **Yes**  
sets | `set` | sets | Non-primitive | **Yes**  
frozen sets | `frozenset` | sets | Non-primitive | No  
|  |  |  |   
functions | `function` | functions | Non-primitive | **Yes**  
`NoneType` | `NoneType` | nulls | _\--?--_ | No  
  
This table shows just a fraction of the available data types. In this book, you will learn about all these types.

The first 4 data types are Python's so-called **primitive** types. Primitive types are the most fundamental data types in a language. Almost all data in a language is built up from these primitive types. For instance, the sequence and mapping types may include primitives and complex types built from those primitives.

Some programmers think of `None` as a primitive type, but that's debatable. We're agnostic on the matter.

The sequences, mappings, and sets are all non-primitive types. In particular, they are also called **collection** types since each collects multiple items in a single object. We'll refer to these types as collections.

Though functions are non-primitives, they are not collections.

The final column of the table shows which types are mutable and which are not. Mutable types are types whose objects can be altered after they are created. So, for example, we can add, remove, and replace elements in a list. Immutable types can't be altered after creation. Instead, you must create a new object with a different value. We'll explore this distinction and its subtleties in greater detail in the [Variables as Pointers](/books/python/read/variables_pointers) chapter.

In this chapter, we'll focus on the primitive types. However, we'll also make a nodding acquaintance with the non-primitive types. First, though, let's talk about literals, and then we'll meet the different primitive types.

## Literals

You can use **literals** to represent most data type values. A literal is any syntactic notation that lets you directly represent an object in source code. For instance, all of the following are literals in Python:
    
    
    'Hello, world!'   # str literal
    3.141592          # float literal
    True              # bool literal
    {'a': 1, 'b': 2}  # dict literal
    [1, 2, 3]         # list literal
    (4, 5, 6)         # tuple literal
    {7, 8, 9}         # set literal
    

Not all objects have literal forms. In those cases, we use the type constructor to create objects of the type. For instance:
    
    
    range(10)         # Range of numbers: 0-9
    range(1, 11)      # Range of numbers: 1-10
    set()             # Empty set
    frozenset([1, 2]) # Frozen set of values: 1 and 2
    

## Numeric Values

**Numeric values** represent numbers. Numbers can be added, subtracted, multiplied, and divided and can be used in a wide variety of mathematical operations. Python also supports other numeric types, such as complex, decimal, and fractional numbers.

Some programming languages treat integers and floating point numbers as a single numeric data type. Python uses different data types to represent numbers. Let's talk about integers first.

### Integers

The integer data type (`int`) represents integers, i.e., the whole numbers (..., -3, -2, -1, 0, 1, 2, 3, ...). Integers do not have a fractional (or decimal) part.
    
    
    1
    2
    -3
    234891234
    131_587_465_014_410_491
    

Note that you can't use commas or periods for grouping: neither `123,456,789` nor `123.456.789` is valid. Instead, you can write the number without separators (`123456789`) or break up the number with underscores (`123_456_789`).

There is no pre-defined limit to the size of an integer. You can have integers with as many digits as will fit in memory, though you may not be able to do much with them then.

### Floats

The floating point data type (`float`) represents floating point numbers, aka, the real numbers. Floating point numbers include integers and numbers with digits after the decimal point.
    
    
    1.0
    1.4142
    -3.14159
    42348.912346
    131_587_465.014_410_491
    

As with integers, you can't use commas or periods for grouping: neither `42,348,912.346` nor `42.348.912,346` is valid. Instead, you can write the number with only a single decimal point (`42348.912346`) or break up the number with underscores (`42_348.912_346`).

#### Working With Big and Small Floats

This section is optional. You probably won't need this information unless you're working on a math- or science-intensive application.

In theory, floats can represent any number, with or without a decimal point. In practice, there are limits that can be looked up in the `sys.float_info` module as follows:
    
    
    import sys
    
    # The maximum number of digits that can be accurately
    # presented
    print(sys.float_info.dig)          # Typically 15
    
    # The largest possible positive float value
    print(sys.float_info.max)          # About 1.8 * (10**308)
    
    # The smallest non-zero positive float value
    print(sys.float_info.min)          # About 2.2 * (10**-308)
    

Don't worry about memorizing those values.

Note that `10**n`, where `n` is positive, represents a 1 followed by `n` zeros. Thus, `10**308` is a 1 followed by 308 zeros; a truly enormous number. On the other hand, `10**-n` is equivalent to the reciprocal of `10**n`, e.g., `1.0 / 10**n`. Thus, `10**-308` is a truly minuscule number.

Python prints extremely large and small floats using **scientific notation** :
    
    
    print(3.14 * (10**20))        # 3.14e+20
    print(3.14 * (10**-20))       # 3.14e-20
    

You can read the `e+20` as meaning 10 to the 20th power, and `e-20` as the reciprocal of 10 to the 20th power.

You can also use scientific notation when writing float literals:
    
    
    print(3.14e+20 / 2.72e-15)    # 1.1544117647058823e+35
    

It's worth pointing out that these floating point issues are not present when working with integers. Integers can be as small or large as you want, provided they fit in memory. Furthermore, integers don't get printed with scientific notation.
    
    
    print(3 * (10**20))           # 300000000000000000000
    

If you want to use scientific notation to write a large integer, you must use the `int` function to convert the number to an integer:
    
    
    print(int(3e+20))             # 300000000000000000000
    

## Variables and Assignment

Most programming languages use something called **variables**. Variables are merely names used to identify values (that is, data). In fact, they are also called **identifiers** , a more general term that applies to variables, constants, function names, class names, and more.

Variables in Python are usually created by **initializing** them to a value. For instance, consider the following code:
    
    
    pi = 3.141592653589793
    life_the_universe_and_everything = 42
    

Here we've created two variables, `pi` and `life_the_universe_and_everything`, then initialized them to the values `3.141592653589793` and `42` respectively.

The syntax used when creating variables, e.g., `foo = 'abc'`, is called **assignment**. We can say that the variable `foo` is assigned to the value `'abc'` or that the value `'abc'` is assigned to the variable `foo`. Both phrases mean the same thing, but the former is usually preferred. However, the latter phrasing is perfectly acceptable. We use both phrasings at Launch School, depending on what reads better in any particular context.

If a particular variable is being assigned a value for the very first time, we may call the assignment an **initialization**. If the variable has already been initialized, we should refer to the assignment as a **reassignment**. For example:
    
    
    foo = 'Hello, world.'         # Assignment or initialization
    foo = "That's all, folks!"    # Reassignment
    

We'll discuss variables and assignment in much more detail later on.

## Boolean Values

**Boolean values** represent binary states such as true or false, on or off, yes or no, one or zero, and so on. The only Boolean values are `True` and `False`.

In Python, booleans sometimes act like numeric values: you can use them in mathematical and comparison expressions. You shouldn't do that, really. However, you can always play with it in the REPL:
    
    
    >>> 3 + True
    4
    
    >>> True == 1
    True
    

Later, we will discuss a related but different concept: _truthiness_. While Boolean values are also truthiness values, truthiness values often aren't Boolean.

Suppose you want to represent the state of a light switch in your application. You can use Boolean values: `True` for on and `False` for off.
    
    
    toggle_on = True
    session_active = False
    

Boolean values have a starring role when working with comparison operators. We'll talk about comparisons in the next chapter. For now, it's enough to know that comparisons check whether a value is equal to, less than, or greater than another value. They return a Boolean result.
    
    
    >>> 5 == 5
    True
    
    >>> 100 < 99
    False
    

## Text Sequences

**Text sequences** are strings of characters, such as words, sentences, dates, foreign text, and so on. They also include things like byte strings, which are sequences of byte-sized values. We don't mention byte strings again in this book.
    
    
    'Hello!'
    "He's pining for the fjords!"
    '1969-07-20'
    

A **string** is a text sequence of Unicode characters. Developers often work with text data like names, messages, and descriptions. Python uses strings to represent such data.

Text sequences can often be treated as ordinary sequences. For instance:
    
    
    greeting = 'hello'
    for letter in greeting:
        print(letter)
    # h
    # e
    # l
    # l
    # o
    

There is one significant difference between a text sequence and an ordinary sequence. Ordinary sequences contain zero or more objects, but a text sequence does not contain any objects: it simply contains the characters (or bytes) that make up the text sequence. Those characters or bytes are not objects; they are simply part of the value.

Proving that the characters of a string are not stored as objects requires studying the Python source code. We're not going to do that.

### String Literals and Dealing With Quotes

You can write string **literals** with single, double, or triple quotes.
    
    
    'Hi there'                      # Single quotes
    "Monty Python's Flying Circus"  # Double quotes
    
    # Triple single quotes
    '''King Arthur: "What is your name?"
    Black Knight: "None shall pass!"
    King Arthur: "What is your quest?"
    Black Knight: "I have no quarrel with you,
                   but I must cross this bridge."
    '''
    
    # Triple double quotes
    """Man: "Is this the right room for an argument?"
    Other Man: "I've told you once."
    Man: "No you haven't!"
    """
    

All of these forms create strings in the same way. Most Python programmers use single quotes as the primary way to write string literals but turn to double quotes when the string's value contains single quotes. However, triple quotes are often used for multi-line strings and a special kind of comment that we won't get into.

You may sometimes need a string that contains both single and double quotes. For instance, if you want to print `My nickname is "Wolfy". What's yours?`, you must consider the fact that the string has both single and double quotes. You can use triple quotes with such a string, or you can escape one of the quote characters like so:
    
    
    print("""My nickname is "Wolfy". What's yours?""")
    print('My nickname is "Wolfy". What\'s yours?')
    print("My nickname is \"Wolfy\". What's yours?")
    

The backslash, or escape character (`\`), tells the computer that the next character isn't syntactic but is part of the string. Escaping a quote prevents Python from seeing it as the string's end. Pay attention to the type of slash you use: a forward slash (`/`) has no significance between quotes. If you want a literal backslash in your string, you must double up the backslashes or use a so-called raw-string literal (we'll discuss raw strings shortly):
    
    
    print("C:\\Users\\Xyzzy")  # Each \\ produces a literal \
    

#### Indexing Strings

You can access the individual characters in a string with the `[]` indexing syntax. The value between the brackets must be an integer between 0 and the length of the string minus 1:
    
    
    >>> my_str = 'abc'
    >>> my_str[0]
    a
    
    >>> my_str[1]
    b
    
    >>> my_str[2]
    c
    
    >>> my_str[4]
    IndexError: string index out of range
    

You can also use negative integers to access characters based on the distance from the end of the string. For instance, `my_str[-1]` returns the last character in the string, while `my_str[-2]` returns the next to last character. The index of the first character is given by `-len(my_str)`:
    
    
    >>> my_str = 'abc'
    >>> my_str[-1]
    c
    
    >>> my_str[-2]
    b
    
    >>> my_str[-3]
    a
    
    >>> my_str[-4]
    IndexError: string index out of range
    

### Raw Strings and f-Strings

String literals with an `r` prefix are **raw string literals**. Raw string literals don't recognize escapes, so you can use literal `\` characters freely.
    
    
    # Both of these print C:\Users\Xyzzy
    print("C:\\Users\\Xyzzy")  # Each \\ produces a literal \
    print(r"C:\Users\Xyzzy")  # raw string literal
    

Raw strings are most often used with Windows-style file names and regular expressions. We cover regular expressions in our Regular Expressions book.

Another prefix you can use with string literals is `f`. It's a recent Python addition for defining **formatted string literals** or, more succinctly, **f-strings**. F-strings enable an operation called **string interpolation**. You create an f-string by preceding the opening quote with the letter `f`:
    
    
    >>> f'5 plus 5 equals {5 + 5}.'
    '5 plus 5 equals 10.'
    
    >>> my_name = 'Karl'
    >>> f'My name is {my_name}.'
    'My name is Karl.'
    
    >>> my_name = 'Clare'
    >>> greeting = 'Ey up?'
    >>> f'{greeting} My name is {my_name}.'
    >>> f'{greeting} My name is {my_name}'
    Ey up? My name is Clare.
    

String interpolation is a handy way to merge Python expressions with strings. The basic syntax is:
    
    
    f'Blah {expression} blah.'
    

Python replaces the `{expression}` substring with the value of the expression inside the braces: it **interpolates** the expression's value. You'll learn to love this feature; it saves time and effort. However, remember that string interpolation is a feature of f-strings only. It doesn't work if you forget the `f` or omit the braces.

You may include as many `{expression}` substrings as needed in an f-string. If you need literal `{` or `}` characters in an f-string, you can escape them by doubling the `{` and `}` characters you want to use as literal characters:
    
    
    foo = 'hello'
    print(f'Use {{foo}} to embed a string: {foo}')
    # Use {foo} to embed a string: hello
    

In the above example, we have an f-string that embeds both `{{foo}}` and `{foo}`. The former gets interpreted as the literal string `{foo}`, while the latter gets replaced by the value of `foo`.

We have two more f-string variants. Earlier in this chapter, we discussed the use of underscores in numbers to make them more readable, e.g., `12_345_678`. However, if you print a number, no matter its size, it won't be printed with underscores (or even commas) unless you use an appropriate f-string:
    
    
    print(f'{123456789:_}')       # 123_456_789
    print(f'{123456789:,}')       # 123,456,789
    

If you use this special form of f-string on a floating point number, only the part before the decimal point will be formatted as expected:
    
    
    print(f'{123456.7890123:_}')  # 123_456.7890123
    print(f'{123456.7890123:,}')  # 123,456.7890123
    

## Functions

**Functions** are chunks of standalone, reusable Python code designed to perform an action. They provide a way to break up your program into modular bits that enable a high degree of code reuse.

One thing that may surprise us is that Python functions have a data type. Many, but not all, languages share this characteristic. We won't discuss this characteristic in this book. However, we will do so in the Core Curriculum.

## None: When You Want Nothing

In programming, we need a way to express the absence of a value. In Python, we do this with `None`. It can also indicate missing, unset, or unavailable data and may sometimes be an error indication.

`None` is a literal whose value is the lone representative of the `NoneType` class.

## Sequences

**Sequences** represent an ordered collection of objects. A sequence's objects can be accessed using a numeric index. In many other languages, the array is the best-known sequence type, but Python uses lists to fill the same role. However, tuples and ranges are also important types.

### Lists and Tuples

Lists and tuples are so similar that we'll cover them together.

Python organizes information into ordered lists using **lists** and **tuples**. Lists and tuples may contain any objects.

**How do I pronounce _tuple_?**

Most people seem to believe that _tuple_ rhymes with _couple_ and _supple_ : TUHP-ul. However, many others say it rhymes with "Mott the Hoople": TOOP-ul. Finally, mathematically-inclined people say it should rhyme with _quadruple_ : TOO-pel. The author tends to switch back and forth between the last two, but Launch School is okay with all 3 pronunciations.

List literals use square brackets `[]` surrounding a comma-delimited list of values, while tuples use parentheses `()`. The comma-delimited list values are known as elements. Let's make a list and a tuple:
    
    
    >>> my_list = [1, 'xyz', True, [2, 3, 4]]
    >>> my_list
    [1, 'xyz', True, [2, 3, 4]]
    
    >>> tup = ('xyz', [2, 3, 4], 1, True)
    >>> tup
    ('xyz', [2, 3, 4], 1, True)
    

Notice that both objects contain a mix of element types, including another list (`[2, 3, 4]`).

List and tuple literals may also use a multi-line format, which is especially useful for more extensive or nested collections:
    
    
    [ # Begin multi-line list literal
        "Monty Python's Flying Circus",
        ( # Begin multi-line tuple literal
          'Eric Idle',
          'John Cleese',
          'Terry Gilliam',
          'Graham Chapman',
          'Michael Palin',
          'Terry Jones',
        ), # End multi-line tuple literal
    ] # End multi-line list literal
    

The trailing comma on the last items in the list and tuple are optional and common practice when writing multi-line collection literals, such as lists, tuples, and dictionaries. Try to be consistent if you use it. It should only be used in multi-line literals.

You can access objects in a list or tuple with the `[]` indexing syntax. The value between the brackets must be an integer between 0 and the length of the sequence minus 1:
    
    
    >>> my_list = [1, 'xyz', True, [2, 3, 4]]
    >>> my_list[0]
    1
    
    >>> my_list[1]
    'xyz'
    
    >>> my_list[2]
    True
    
    >>> my_list[3]
    [2, 3, 4]
    
    >>> my_list[4]
    IndexError: list index out of range
    

A crucial distinction between lists and tuples is that lists are mutable. Tuples, however, are immutable.

One way to mutate a list is to use the indexing syntax to the left of the `=` in an assignment. This is called **indexed reassignment** or **element reassignment**. (We usually prefer _element reassignment_ , but you will often hear and read about _indexed reassignment_.) For instance:
    
    
    >>> my_list[3] = 'New value'
    >>> my_list
    [1, 'xyz', True, 'New value']
    
    >>> tup[3] = 'New value'
    TypeError: 'tuple' object does not support item
    assignment
    

The immutability of tuples limits their usefulness slightly, but Python can perform more optimizations on tuples. The optimizations can reduce storage requirements and improve performance.

Here's a bit of Python weirdness: if you want to use a literal to create a tuple with one element, you can't simply write:
    
    
    my_tuple = (1)
    print(type(my_tuple))        # <class 'int'>
    

In this case, the parentheses cause Python to treat the expression as a parenthesized expression, not as a tuple literal. To define a one-element tuple, you must place a comma after the element value:
    
    
    my_tuple = (1,)
    print(type(my_tuple))        # <class 'tuple'>
    

The most important facts to remember about lists and tuples are:

  * The order of the elements is significant. 
  * Lists are mutable; tuples are immutable. 
  * Use indexing syntax to retrieve specific elements. 
  * Use indexing syntax to reassign specific list elements. 
  * Index numbers are non-negative integers starting from `0` and ending at the sequence's length minus 1. (Later, we will learn that negative integers are also allowed. For now, though, we'll only use non-negative integers.) 



### Ranges

A **range** is a sequence of integers between two endpoints. Ranges are most commonly used to iterate over an increasing or decreasing range of integers. Let's see how we can create some ranges:
    
    
    >>> tuple(range(5))
    (0, 1, 2, 3, 4)
    
    >>> tuple(range(5, 10))
    (5, 6, 7, 8, 9)
    
    >>> list(range(1, 10, 2))
    [1, 3, 5, 7, 9]
    
    >>> list(range(0, -5, -1))
    [0, -1, -2, -3, -4]
    

With one argument, the range starts from 0 and ends just before the argument. Thus, `range(5)` goes from 0 through 4.

With two arguments, the first argument is the starting point, while the second argument is one past the last number in the range. Thus, `range(5, 10)` goes from 5 through 9.

With three arguments, the 3rd argument is a step value. Thus, `range(1, 10, 2)` goes from 1 through 9 with a step of 2 between the numbers. On the other hand, `range(0, -5, -1)` goes from 0 through -4 with a step of -1. This results in a range that goes from the highest value to the lowest.

Python optimizes ranges to save memory; it doesn't need the integers before a program asks for them. One way to get those numbers is to convert the range to a list or tuple. This is why we used the `list` and `tuple` functions to expand each range; either will suffice.

Like strings, lists, and tuples, you can use indexing syntax to access specific numbers in a range object:
    
    
    >>> my_range = range(5, 10)
    >>> my_range[3]               # 8
    

## Mappings

**Mappings** represent an unordered collection of objects stored as key-value pairs. Each key (usually a string) provides a unique identifier for a specific object in the mapping. The value is the object associated with that key.

The dictionary (class `dict`) is the most common mapping in Python. It's the only kind of mapping we'll see in this book.

A **dictionary** (**dict**) is a collection of key-value pairs. A dict is similar to a list but uses keys instead of indexes to access specific elements. Other languages use different names for similar structures: hashes, mapping, objects, and associative arrays are the most common terms. Essentially, a Python dictionary is a collection of key-value pairs.

You can create dictionaries using dict literals. They have zero or more key-value pairs separated by commas, all embedded within curly braces (`{}`). A key-value pair associates a key with a specific value. Key-value pairs in dict literals use the key followed by a colon (`:`) and then the value.

That sounds more complicated than it is. Let's put those words into action. Type along!

Our example creates a dict with three key-value pairs:
    
    
    >>> my_dict = {
    ...     'dog': 'barks',
    ...     'cat': 'meows',
    ...     'pig': 'oinks',
    ... }
    {'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}
    

This dict contains 3 keys: the strings `'dog'`, `'cat'`, and `'pig'`. The `'dog'` key is mapped to the string `'barks'` while `'cat'` is mapped to `'meows'`

Dictionary literals may also use a multi-line format, which is especially useful for larger or nested dictionaries:
    
    
    my_dict = {
        'title': "Monty Python's Flying Circus",
        'cast': [
            'Eric Idle',
            'John Cleese',
            'Terry Gilliam',
            'Graham Chapman',
            'Michael Palin',
            'Terry Jones',
        ],
        'first_season': 1969,
        'last_season': 1974,
        'reboot_season': None,
    }
    

You can access objects in a dict with the `[]` key access syntax. The value between the brackets must be one of the keys in the dict:
    
    
    >>> my_dict = {
    ...     'dog': 'barks',
    ...     'cat': 'meows',
    ...     'pig': 'oinks'
    ... }
    ...
    >>> my_dict['cat']
    'meows'
    
    >>> my_dict['bird']
    KeyError: 'bird'
    

You can use the same key access syntax on the left side of an assignment to replace the associated key's value with a different object:
    
    
    >>> my_dict['cat'] = 'purrs'
    >>> my_dict
    {'dog': 'barks', 'cat': 'purrs', 'pig': 'oinks'}
    

As of Python 3.7, dictionary key/value pairs are stored in the same order they are inserted into a dictionary; before 3.7, the key/value pair order was unpredictable. This can be interpreted as meaning that dictionaries are ordered. However, even with this ordering, the key/value pair order can change. For instance:
    
    
    dic = {}
    dic['a'] = 1
    dic['b'] = 2
    print(dic)          # {'a': 1, 'b': 2}
    del dic['a']
    dic['a'] = 1
    print(dic)          # {'b': 2, 'a': 1}
    

For this reason, we prefer to categorize dictionaries (and other mappings) as unordered collections. Dictionaries, in particular, are unordered collections in which **insertion order is preserved**.

**One last note** : You can use almost any immutable object as a key in a dict; it doesn't have to be a string. The only significant requirement for keys is that they are **hashable**. We discuss hashing in our PY110 course. For now, though, the important concept is that immutable types are almost always hashable, while mutable types are almost always non-hashable. Thus, since lists are mutable and, therefore, unhashable, you can't use a list as a dictionary key. However, you can use a tuple as a dictionary key provided all of its elements are immutable and hashable.

## Sets

**Sets** represent an unordered collection of unique objects; the objects are sometimes called the **members** of the set. Sets are similar to mappings, except instead of using keys and values, a set is simply a collection of immutable (and _hashable_ , as mentioned above) objects.

As the name suggests, sets support several operations corresponding to mathematical sets: unions, intersections, etc. We won't discuss those in this book.

The literal syntax for sets is a comma-separated list of object values between curly braces (`{}`). As a special case, empty sets must be created with the `set` constructor since `{}` by itself is an empty dictionary. Let's see how it's done:
    
    
    >>> d1 = {}         # Empty dict
    >>> print(type(d1))
    <class 'dict'>
    
    >>> s1 = set()      # Empty set
    >>> print(s1)
    set()
    
    # Create a set from a literal
    >>> s2 = {2, 3, 5, 7, 11, 13}
    >>> print(s2)
    {2, 3, 5, 7, 11, 13}
    
    # Create a set from a string
    >>> s3 = set("hello there!")
    {'t', 'o', 'e', 'l', ' ', 'h', '!', 'r'}
    

In the last example, notice that the set only contains one occurrence of each character, even though the string has repeated instances of some characters. Set members are always unique, even if you try to add duplicates. This example also shows that the order of the characters in the set has nothing to do with the order of the characters in the string.

Set literals may also use a multi-line format, which is especially useful for larger sets:
    
    
    monty_python_cast = {
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    }
    

There are two main set types: ordinary sets (class `set`) and frozen sets (class `frozenset`). Frozen sets are merely immutable sets. They also lack a literal syntax: you must use the `frozenset` function to create one.
    
    
    >>> s5 = frozenset([1, 2, 3])
    >>> print(s5)
    frozenset({1, 2, 3})
    
    >>> s6 = frozenset((1, 2, 3))
    >>> print(s6)
    frozenset({1, 2, 3})
    
    >>> s7 = frozenset({1, 2, 3})
    >>> print(s7)
    frozenset({1, 2, 3})
    
    >>> s8 = frozenset(range(1, 4))
    >>> print(s8)
    frozenset({1, 2, 3})
    

Note that you can initialize a set or frozen set with any iterable type. In the most recent examples, we initialize a frozen set using a list, a tuple, a set, and a range. However, when printing frozen sets, they are always represented as using a set to initialize the frozen set.

**One last note** : You can use almost any immutable value as a set member. The only significant requirement is that the objects must be hashable.

## Summary

We've learned about Python's fundamental data types in this chapter. We've learned how to create these objects but not how to use them. That's our task in the next chapter. First, though, we have a few exercises for you.

##  Exercises

  1. Identify the data type or class for each of the following values:

Value  
---  
`'True'`  
`False`  
`(1, 2, 3)`  
`1.5`  
`[1, 2, 3]`  
`2`  
`range(5)`  
`{1, 2, 3}`  
`None`  
`{'foo': 'bar'}`  
  
#### Solution

Value | Type | Class  
---|---|---  
`'True'` | String | `str`  
`False` | Boolean | `bool`  
`(1, 2, 3)` | Tuple | `tuple`  
`1.5` | Float | `float`  
`[1, 2, 3]` | List | `list`  
`2` | Integer | `int`  
`range(5)` | Range | `range`  
`{1, 2, 3}` | Set | `set`  
`None` | `NoneType` | `NoneType`  
`{'foo': 'bar'}` | Dictionary | `dict`  
  
Notice that the first item is not a Boolean value - the quotes make it a string.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Create a tuple called `names` that contains several pet names. For instance:

Name  
---  
Asta  
Butterscotch  
Pudding  
Neptune  
Darwin  
  
You can use that data or make up your own.

#### Solution
    
        names = ('Asta', 'Butterscotch', 'Pudding', 'Neptune', 'Darwin')
    
    
        names = (
        'Asta',
        'Butterscotch',
        'Pudding',
        'Neptune',
        'Darwin',
    )
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Create a dictionary named `pets` that contains a list of pet names and the type of animal. For instance:

Name | Animal  
---|---  
Asta | dog  
Butterscotch | cat  
Pudding | cat  
Neptune | fish  
Darwin | lizard  
  
You can use that data or make up your own.

#### Solution
    
        pets = {'Asta': 'dog', 'Butterscotch': 'cat', 'Pudding': 'cat', 'Neptune': 'fish', 'Darwin': 'lizard'}
    
    
        pets = {
        'Asta':         'dog',
        'Butterscotch': 'cat',
        'Pudding':      'cat',
        'Neptune':      'fish',
        'Darwin':       'lizard',
    }
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Basic Operations

Almost all Python data types provide a variety of operations that you can perform on objects of that type. In the previous section, we learned about Python's basic data types. However, we haven't done anything that shows how they are used. We'll do something about that in this chapter.

A remarkable feature of Python is how much functionality the different types share. For instance:

  * You can compare almost any pair of objects with the same type for equality and, in many cases, for less than or greater than operations. 
  * You can determine the length of any collection object or text sequence by calling the `len()` function on that object. 
  * You can convert nearly any object into a human-readable string form. 
  * You can iterate over different collection types without changing your syntax. 



This feature brings considerable flexibility and ease of programming to the language.

In this chapter, we'll begin to distinguish between three main kinds of types:

  * The **built-in** types are part of Python. They are available in every program if you want them; just start using them. Most types we'll encounter in this book are built-in types. 
  * The **standard** types aren't automatically loaded when running `python`. Instead, they are available from modules you can import into your programs. You don't have to download the standard types, but you do need to import them. We'll see some examples of importing modules in this chapter and learn more about importing modules later in the book. 
  * The **non-standard** types come from either you and your colleagues or as downloadable modules available on the Internet. 



## Arithmetic Operations

First up, let's turn our attention to the elementary arithmetic operations. All built-in and standard numeric data types work with all or most of these operations:

Operator | Operation  
---|---  
`+` | Addition  
`-` | Subtraction  
`*` | Multiplication  
`/` | Division  
`//` | Integer division  
`%` | Modulo  
`**` | Exponentiation  
  
These operators work with the built-in integer and float types and other types like the complex, decimal, and fractional number types. We'll focus on integers and floats here, but working with other data types is nearly identical.

Let's look at some examples of the basic operations in action:

  * Addition
    
        print(38 + 4)      # 42
    print(38.4 + 41.9) # 80.3
    
    # mixing integers & floats
    print(38 + 41.5)   # 79.5
    

  * Subtraction
    
        print(38 - 4)      # 34
    print(38.4 - 41.9) # -3.5
    
    # mixing integers & floats
    print(38 - 41.5)   # -3.5
    

  * Multiplication
    
        print(38 * 4)      # 152
    print(38.4 * 41.1) # 1578.24
    
    # mixing integers & floats
    print(38 * 41.5)   # 1577.0
    

  * Division with `/`
    
        print(16 / 4)      # 4.0
    print(16 / 2.5)    # 6.4
    

When you divide two integers, two floats, or one of each with `/`, the result is always a float, even if both operands are integers.

  * Integer division with `//`
    
        print(16 // 3)     # 5
    print(16 // -3)    # -6
    print(16 // 2.3)   # 6.0
    print(-16 // 2.3)  # -7.0
    

The `//` operator returns the largest whole number less than or equal to the floating point result. That is, it rounds the result down to the nearest whole number. Thus, `16 // 3` returns `5`, not `5.333333333333333`. Likewise, `16 // -3` returns `-6`. If either operand is a float, the return value is also a float, but it's still rounded down to a whole number.

**Note** : The `//` operator doesn't work with the built-in complex numbers.

  * Exponentiation (powers)

The expression `a**b` tells Python to raise `a` to the power of `b`. Thus, something like `3**4` means 3 to the 4th power, or 3 * 3 * 3 * 3 or 81.
    
        print(16**3)     # 4096
    

  * Modulo

The `%` operator is called the **modulo operator**. It is sometimes called the **modulus operator** or the **remainder operator** , both of which are technically incorrect. (There are some [subtle differences](https://math.stackexchange.com/questions/801962/difference-between-modulus-and-remainder) between modulo and remainder operations). This confusion is understandable since the `%` operator is usually used to calculate the remainder of dividing two integers:
    
        print(15 % 3)   # 0
    print(16 % 3)   # 1
    print(17 % 3)   # 2
    print(18 % 3)   # 0
    

We won't get into the differences between modulo, modulus, and remainder in this book. What's important right now is that `%` is easiest to understand when the operands are both positive integers.

When both `a` and `b` are positive integers, `a % b` returns the non-negative remainder of dividing `a` by `b`. Of special interest is that `a % b` returns `0` if, and only if, `a` is exactly divisible by `b`. If either `a` or `b` is negative, things get weird, as can be seen in the following table:

a | b | a % b | remainder  
---|---|---|---  
14 | 7 | 0 | 0  
17 | 7 | 3 | 3  
17 | -7 | -4 | 3  
-17 | 7 | 4 | -3  
-17 | -7 | -3 | -3  
  
The final column in the above table shows what a remainder operator would return if Python had one. You can compute the remainder in Python using the `math` module's `remainder` function:
    
        from math import remainder
    
    print(int(remainder(14, 7)))    # 0
    print(int(remainder(17, 7)))    # 3
    print(int(remainder(17, -7)))   # 3
    print(int(remainder(-17, 7)))   # -3
    print(int(remainder(-17, -7)))  # -3
    

In general, you don't need to know the difference between modulo and remainder; just be aware that they are different. You also don't need to worry about how they work with negative numbers if you can avoid using negative numbers. Since most use cases of `%` only care about divisibility, that will happen naturally. If `a % b == 0`, then `a` is evenly divisible by `b`, no matter the signs of `a` and `b`.

**Note** : The `%` operator doesn't work with the built-in complex numbers.




### Floating Point Imprecision

Floating point numbers have some precision issues you must be aware of. For instance, if you add `0.1` and `0.2` and compare the result for equality with `0.3`, you'll learn that they are **not** equal:
    
    
    print(0.1 + 0.2 == 0.3)       # False
    

This can be a serious problem in some applications, such as finance. It's an artifact of how real numbers are stored on most computers; you'll encounter this problem in almost every language. One way around the problem in Python is to use the `math.isclose` function:
    
    
    import math
    math.isclose(0.1 + 0.2, 0.3)  # True
    

You can also use the `decimal.Decimal` type to make precise computations:
    
    
    from decimal import Decimal
    Decimal('0.1') + Decimal('0.2') == Decimal('0.3')
    # True
    

Note that you should always use strings with `decimal.Decimal`. You can use float values. However, you will lose the benefit of precise computation if you do.

## Equality Comparison

You sometimes want to determine whether two values are identical or different. The `==` and `!=` operators can help with that. `==` compares two operands for equality and returns `True` or `False` as appropriate. In contrast, `!=` returns `True` if they are not equal, `False` otherwise.

Let's try some comparisons in Python:
    
    
    print(42 == 42)       # True
    print(42 == 43)       # False
    print('foo' == 'foo') # True (works with strings)
    print('FOO' == 'foo') # False (Case matters)
    
    
    
    print(42 != 42)       # False
    print(42 != 43)       # True
    print('foo' != 'foo') # False (works with strings)
    print('FOO' != 'foo') # True (Case matters)
    

The operators `==` and `!=` work with almost all data types. Assuming that the values represented by `a` and `b` below are instances of the built-in data types, then:

  * If `a` and `b` have different data types, `a == b` usually returns `False` while `a != b` returns `True`. However, numbers are an exception: all built-in and standard number types can be compared for equality without regard to their specific types. Thus, `1 == 1.0` is `True`.

  * If `a` and `b` have the same data type, `a == b` almost always returns `True` if the two objects have the same value, while `a != b` returns `False`.




When working with standard and non-standard types, all bets are off. While most non-builtin types obey the same rules, not all do. The only way to be sure is to study the documentation, look at the source code, or try to determine the behavior from tests.

## Ordered Comparisons

As you might expect, Python supports several other comparison operations: you can check for less than (`<`), less than or equal to (`<=`), greater than (`>`), and greater than or equal to (`>=`):
    
    
    print(42 < 41)           # False
    print(42 < 42)           # False
    print(42 <= 42)          # True
    print(42 < 43)           # True
    
    print('abcdf' < 'abcef') # True
    print('abc' < 'abcdef')  # True
    print('abcdef' < 'abc')  # False
    print('abc' < 'abc')     # False
    print('abc' <= 'abc')    # True
    print('abd' < 'abcdef')  # False
    print('A' < 'a')         # True
    print('Z' < 'a')         # True
    
    print('3' < '24')        # False
    print('24' < '3')        # True
    

Note the comparisons involving strings. Strings are compared **lexicographically** , which means they are compared character-by-character from left-to-right.

For instance, on line 6, we first compare the first character of each string (`'a'`). Since they are the same, we move on to the next pair of characters (`'b'`), then the pair after that (`'c'`). Everything is equal up to this point.

However, when we compare `'d'` against `'e'`, we finally see a difference between the two strings. Since `'d' < 'e'`, the final result is `True`. Python doesn't bother looking at the remaining character in these strings (`'f'`).

This lexicographic comparison also explains why `'3' < '24'` on line 15 is `False` and `'24' < '3'` on line 16 is `True`. Only the first character of each string gets compared.

It's also worth looking at `'abc' < 'abcdef'` on line 7. While the first 3 characters of both strings are the same, the first string is shorter than the second. When Python compares two strings that are equal up to the length of the shorter string, then the shorter string is deemed to be less than the longer string.

When comparing strings, Python stops as soon as it makes a decision. For instance, in `'abd' < 'abcdef'`, Python only needs to check the first 3 characters in both strings. When it reaches the 3rd character, it can see that `'abd'` is _not_ less than `'abcdef'`.

Finally, lines 12 and 13 help demonstrate that uppercase alphabetic letters are considered to be less than lowercase alphabetic letters. Every uppercase letter is less than every lowercase letter. This behavior often confuses new programmers, but almost all languages work this way.
    
    
    print(42 > 41)           # True
    print(42 > 42)           # False
    print(42 >= 42)          # True
    print(42 > 43)           # False
    
    print('abcdf' > 'abcef') # False
    print('abc' > 'abcdef')  # False
    print('abcdef' > 'abc')  # True
    print('abc' > 'abc')     # False
    print('abc' >= 'abc')    # True
    print('abcdef' > 'abd')  # False
    print('A' > 'a')         # False
    print('Z' > 'a')         # False
    
    print('3' > '24')        # True
    print('24' > '3')        # False
    

Let's look more closely at `'abcdef' > 'abc'`. In this example, the strings have unequal sizes. Furthermore, the longer string is identical up to the shorter string's length. Python returns `True` here; when it can no longer take characters from the shorter string, it concludes that the longer string has the greater value. Similar behaviors occur with the other ordered comparison operators.

It's also worth noting that even numeric strings are compared character by character. Thus, `'3' > '24'` returns `True` since the character `3` is greater than the character `2`.

In general, numeric characters in a string are less than alphabetic characters, and uppercase letter characters are less than lowercase letters. Other characters appear at different points. For instance, `'#' < '5' < ';' < 'A' < '^' < 'a'`. (You don't have to memorize this.)

If the precise ordering of character values becomes sufficiently significant to matter, look them up in a [standard ASCII table](https://www.ascii-code.com/ASCII).

As with `==` and `!=`, many other types besides numbers and strings work with the ordered comparison operators. For instance, you can compare sets with these operators to determine if set a is a subset or superset of set b. You can also compare lists and tuples: like string comparisons, list and tuple comparison goes element by element to determine which object is less than or greater than the other:
    
    
    print({3, 1, 2} < {2, 4, 3, 1})         # True
    print({3, 1, 2} > {2, 4, 3, 1})         # False
    print({2, 4, 3, 1} > {3, 1, 2})         # True
    
    
    
    print([1, 2, 3] < [1, 2, 3, 4])         # True
    print([1, 4, 3] < [1, 3, 3])            # False
    print([1, 3, 3] < [1, 4, 3])            # True
    

## String Concatenation

String concatenation looks like numeric addition and multiplication, but the result is entirely different. It uses the `+` and `*` operators to join strings.

Back to Python:
    
    
    >>> 'foo' + 'bar'
    'foobar'
    

That looks simple enough.

There is at least one surprise you may encounter. What will the following code return? Try answering before you try it.
    
    
    '1' + '2'
    

If you thought it would return `3`, that makes sense. However, since `'1'` and `'2'` are both strings, Python performs concatenation instead. That's why the result is `'12'`.

You can also use the `*` operator to perform repetitive concatenation. For instance, if you want the string `'abcabcabc'`, you can use `*` to generate it:
    
    
    print('abc' * 3)              # 'abcabcabc'
    print(3 * 'abc')              # 'abcabcabc'
    

## Coercion

Suppose you have two string values in your program, `'1'` and `'2'`, that you want to add mathematically and get `3`. You can't do that directly since `+` performs concatenation when its operands are both strings. Somehow, we need to coerce the strings `'1'` and `'2'` to the numbers `1` and `2`: we want to perform a **type coercion**.

### Strings to Numbers

The `int` and `float` functions coerce a string to a number. `int` coerces a string to an integer, while `float` coerces a string to a float.
    
    
    print(int('5'))               # 5
    print(float('3.141592'))      # 3.141592
    

These functions take a string or another number and attempt to convert it to an integer or a float. You can then perform arithmetic operations on the result.

### Numbers to Strings

You can also coerce numbers into strings. The `str` function provides this capability. Let's see an example:
    
    
    print(str(5))                 # '5'
    print(str(3.141592))          # '3.141592'
    

In reality, `str` can convert most Python values to a valid string. We'll see more situations where you can use `str` later.

### Implicit Coercion

Using functions like `str`, `int`, etc., to coerce values from one type to another is sometimes called **explicit coercion**. It's required for many conversions and a good idea in others where clarity is needed.

Python also has **implicit coercions**. Implicit coercions can be handy; they can save a lot of typing and often lead to more readable code. For instance, when you use `print()` to print an object -- any object -- `print` will implicitly coerce it to a string before printing it. That saves considerable typing:
    
    
    # (Unnecessary) Explicit coercion
    print(str(3))           # 3
    print(str(False))       # False
    print(str([1, 2, 3]))   # [1, 2, 3]
    print(str({4, 5, 6}))   # {4, 5, 6}
    
    # Implicit coercion
    print(3)                # 3
    print(False)            # False
    print([1, 2, 3])        # [1, 2, 3]
    print({4, 5, 6})        # {4, 5, 6}
    

Implicit coercion also occurs when mixing numbers of different types in an expression:

Type A | Type B | Result type  
---|---|---  
int | float | float  
int | Decimal | Decimal  
int | Fraction | Fraction  
float | Decimal | \--error--  
float | Fraction | float  
Decimal | Fraction | \--error--  
  
These results aren't surprising. Mixing different number types is handy, and most people expect it.

Gotchas sometimes arise with implicit coercion. One such gotcha occurs when you use a Boolean in an arithmetic expression. Python implicitly coerces `True` to the integer value 1 and `False` to 0. The resulting integer may be coerced further based on the types of the other subexpressions.
    
    
    print(True + True + True)     # 3
    print(True + 1 + 1.0)         # 3.0
    print(False * 5000)           # 0
    

If there's any chance that one of your variables contains a Boolean value, be careful. While Python won't mind, the result may not be what you expect. Even if you expect it, will the next person who looks at your code?

One last implicit coercion is the truthiness coercion. Python can use any value, regardless of type, in a conditional expression in an `if` or `while` statement. We'll discuss this in the [Truthiness topic](/books/python/read/flow_control#truthiness) of the Flow Control chapter.

## Determining Types

As we've seen, Python data types give the programmer many choices. However, when things go wrong and you need to debug your code, you may have to determine what classes you're working with. Knowing how to view type information in the REPL is worthwhile even if you aren't debugging code. You can even make programmatic decisions based on type. However, that's usually a sign of a problem with your design.

With that said, let's see some of the ways we can determine types. First up is the `type` function, which can be called with any object:
    
    
    print(type(1))         # <class 'int'>
    print(type(3.14))      # <class 'float'>
    print(type(True))      # <class 'bool'>
    print(type('abc'))     # <class 'str'>
    print(type([1, 2, 3])) # <class 'list'>
    print(type(None))      # <class 'NoneType'>
    
    foo = 42               # Variables work, too
    print(type(foo))       # <class 'int'>
    

Note that the return value usually includes more information than you need. If you just want the class name, you can access the `__name__` property from the result:
    
    
    print(type('abc').__name__)   # str
    print(type(False).__name__)   # bool
    print(type([]).__name__)      # list
    

Finally, you can use `type` with the `is` operator.
    
    
    print(type('abc') is str)     # True
    print(type('abc') is int)     # False
    print(type(False) is bool)    # True
    print(type([]) is list)       # True
    print(type([]) is set)        # False
    

Note that all 3 of the above approaches discount the effects of inheritance. Since we don't discuss inheritance in this book, that doesn't matter for now. However, you may want to consider using the `isinstance` function, which determines whether an object is an instance of a particular type. It takes inheritance into account. We'll return to this in our [Object Oriented Programming book](/books/oo_python/).
    
    
    print(isinstance('abc', str))    # True
    print(isinstance([], set))       # False
    
    class A:
        pass
    
    class B(A):
        pass
    
    b = B()
    
    print(type(b).__name__) # B
    print(type(b) is B)     # True
    print(type(b) is A)     # False (b's type is
                            # not A)
    print(isinstance(b, B)) # True
    print(isinstance(b, A)) # True (b is instance of A and B)
    

## String Representations

You can use the `str` and `repr` functions with any object. They each return a string representation of an object. The `str` function returns a string intended to be something that humans can read. It is often used when printing an object. Python implicitly calls `str()` when it needs to print or interpolate a value. The `repr` function is a bit lower-level. It returns a string that you can, in theory, use to create a new instance of the object.

For most built-in types, `str` and `repr` return the same value. However, that is not always the case. Strings are one of the more obvious types with different `str` and `repr` return values:
    
    
    my_str = 'abc'
    print(my_str)       # abc
    print(str(my_str))  # abc (same as print(my_str))
    print(repr(my_str)) # 'abc' (note the quotes)
    

## Collection and String Lengths

All built-in collection types (strings, sequences, mappings, and sets) have lengths. The length of a string is the number of characters in the string, while the length of other collections is the number of elements in the collection. You can easily determine the length of a collection using the `len` function:
    
    
    print(len('Launch School'))       # 13 (string)
    print(len(range(5, 15)))          # 10 (range)
    print(len(range(5, 15, 3)))       # 4 (range)
    print(len(['a', 'b', 'c']))       # 3 (list)
    print(len(('d', 'e', 'f', 'g')))  # 4 (tuple)
    print(len({'foo': 42, 'bar': 7})) # 2 (dict)
    print(len({'foo', 'bar', 'qux'})) # 3 (set)
    

## Indexing and Key Access

Strings, ranges, lists, and tuples all support indexed access to individual elements in the collection. Indices begin at 0 and run through 1 less than the length of the string or collection. Any index used must be in this range, or you will get an `IndexError`:

Indices may also be negative in the range `-1` to `-len(seq)`. We'll discuss this later.
    
    
    my_str = "abc"                # string
    print(my_str[0])              # 'a'
    print(my_str[1])              # 'b'
    print(my_str[2])              # 'c'
    print(my_str[3])
    # IndexError: string index out of range
    
    
    
    my_range = range(5, 8)         # range
    print(my_range[0])             # 5
    print(my_range[1])             # 6
    print(my_range[2])             # 7
    print(my_range[3])
    # IndexError: range object index out of range
    
    
    
    my_list = [4, 5, 6]           # list
    print(my_list[0])             # 4
    print(my_list[1])             # 5
    print(my_list[2])             # 6
    print(my_list[3])
    # IndexError: list index out of range
    
    
    
    tup = (8, 9, 10)              # tuple
    print(tup[0])                 # 8
    print(tup[1])                 # 9
    print(tup[2])                 # 10
    print(tup[3])
    # IndexError: tuple index out of range
    

Dictionaries use keys that work similarly to indexes. However, it is incorrect to describe dictionary keys as indexes: they are keys. As with indexes, using a key that does not exist in the dictionary produces an error:
    
    
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict['a'])           # 1
    print(my_dict['b'])           # 2
    print(my_dict['c'])           # 3
    print(my_dict['d'])           # KeyError: 'd'
    

### Using [] to Update Elements

Since they are mutable, lists and dictionaries let you use the `[]` operator to replace collection elements. As you might expect, lists use indexes to update elements, while dictionaries use keys. You cannot use `[]` to create new list elements, but you can do so with dictionaries.

Note that strings, ranges, tuples, and frozen sets are immutable, so they do not support using `[]` for updates. Sets are mutable, but they don't support indexing.
    
    
    my_list = [1, 2, 3, 4]
    my_list[2] = 6
    print(my_list)          # [1, 2, 6, 4]
    my_list[4] = 10
    # IndexError: list assignment index out of range
    
    
    
    my_dict = {
        'dog': 'barks',
        'cat': 'meows',
        'pig': 'oinks',
    }
    
    my_dict['pig'] = 'snorts'
    print(my_dict)
    # Pretty printed for clarity
    # {
    #     'dog': 'barks',
    #     'cat': 'meows',
    #     'pig': 'snorts'
    # }
    
    my_dict['fish'] = 'glub glub'
    print(my_dict)
    # Pretty printed for clarity
    # {
    #     'dog': 'barks',
    #     'cat': 'meows',
    #     'pig': 'snorts',
    #     'fish': 'glub glub'
    # }
    

## Expressions and Statements

The distinction between statements and expressions in Python is fundamental and affects how you write and structure your code. Let's define them now.

An **expression** combines values, variables, operators, and calls to functions to produce a new object. Expressions must be evaluated to determine the expression's value. Examples of expressions include:

  * Literals: `5`, `'Karl'`, `3.141592`, `True`, `None`
  * Variable references: `foo` or `name` when these variables have been previously defined. 
  * Arithmetic operations: `x + y` or `a * b - 5`. 
  * Comparison operations: `'x' == 'x'` or `'x' < 'y'`. 
  * String operations: `'x' + 'y'` or `'x' * 32`. 
  * Function calls: `print('Hello')` or `len('Python')`. 
  * Any valid combination of the above that evaluates to a single object. 



You can think of an expression as something that produces a value that can be assigned to a variable, passed to a function or method, or returned by a function or a method.

A **statement** , on the other hand, is an instruction that tells Python to perform an action of some kind. Unlike expressions, statements don't return values. They do something but don't produce a value as expressions do.

Examples of statements include:

  * Assignment: like `x = 5`. This doesn't evaluate as a value; it assigns a value to a variable. 
  * Control flow: such as `if`, `else`, `while`, `for`, and so on. These determine the flow of your program but don't evaluate as a value themselves. 
  * Function and class definitions: using `def` or `class`. 
  * Return statements: like `return x`, which tells a function to exit and return a value. `return` itself doesn't return a value; it informs the function what value it should return. 
  * Import statements: such as `import math`. 



There are some key differences to keep in mind:

  * Expressions always return a value; statements do not. 
  * Expressions are often part of statements. For example, in the statement `y = x + 5`, `x + 5` is an expression. 
  * Statements often represent bigger chunks of functionality like loops or conditionals; expressions deal with determining values. 



Some expressions are stand-alone. They aren't part of an ordinary statement, but their return values are ignored. These stand-alone expressions fall into a gray area; the return values are ignored, making them seem more like statements. In this book and elsewhere at Launch School, we consider these stand-alone expressions as both expressions and statements.
    
    
    3 + 4            # Simple expression
    print('Hello')   # Function call; returns None
    my_list.sort()   # Method call; returns None
    

## Expression Evaluation

By default, Python evaluates most expressions from left to right. This is fine if all of the operators in an expression are the same operator:
    
    
    >>> 1 + 2 + 3 + 4 + 5
    15
    

Here, Python first evaluates `1 + 2`, which is `3`. It then adds `3` to the first `3`, which yields `6`. Next, we add `4` to get `10` and, finally, we add `5` to get `15`.

However, what happens if the operators are mixed?
    
    
    >>> 4 * 5 - 1 + 2 * 3
    ??
    

Should that expression be `63`? Is the result possibly `72`? `25`? `-8`? Maybe it's something else altogether? No, this isn't one of those silly math puzzles you see on social media.

Python evaluates that expression as `25`: the multiplications occur first (`4 * 5` is `20` and `2 * 3` is `6`), followed by the additions and subtractions from left to right (`20 - 1 + 6` is `25`). Python dictates this order of evaluation through its precedence rules, which we discuss in more detail in the Core Curriculum.

You shouldn't rely on the precedence rules even if you've memorized them. Use parentheses to tell Python explicitly how you want to evaluate the expression:
    
    
    print(((4 * 5) - 1) + (2 * 3))   # 25
    print((4 * ((5 - 1) + 2)) * 3)   # 72
    print(((((4 * 5) - 1) + 2) * 3)) # 63
    print(4 * (5 - (1 + (2 * 3))))   # -8
    

Parenthesized sub-expressions are usually evaluated before any non-parenthesized sub-expressions. So, on line 1 above, Python evaluates `(4 * 5)` and (`2 * 3)` before it performs any addition or subtraction operations.

Nested parenthesized sub-expressions are evaluated before the parenthesized expressions they are contained in. Thus, on line 1 above, `(4 * 5)` and `(2 * 3)` get evaluated first. Next, `1` gets subtracted from the result of `(4 * 5)`, then the result of `(2 * 3)` gets added to that value.

In general, you should not depend on the precedence rules in Python. No matter how well you know them, you will eventually forget one of the trickier cases, and readers of your code may not understand the code. You should **always** use parentheses to inform Python and readers of your code of your intent.

## Output vs. Return Values

Inexperienced programmers are often confused with the difference between returning or outputting a value. When we invoke the `print` function, we're telling Python to write some output to the display. In Python, that is usually your screen. The term **log** is often used as a synonym for printing or showing something on the display. Sometimes, we even use log, the noun, as a synonym for your terminal screen. For example, in the following code, the `print` function simply prints the string `'abc'`. It doesn't return a useful value; it's sole purpose is to print something.
    
    
    print('abc')
    

In many cases, a function or expression doesn't print anything, but simply returns a value that gets assigned to a variable, evaluated as a condition, or passed to another function. For example, the following code first calls the `range` function, which returns a `range` object. That value is subsequently passed to the `list` function which, in turn, returns a `list` object.
    
    
    list(range(3))
    

In the Python REPL, the return value can also be displayed on the screen. However, take care not to confuse these return values with actual output. It's simply the REPL's way of showing you that an expression returned a value. If you run the code from a file, you won't see these return values.

## Summary

This chapter covered the basic building blocks of Python. You learned how to perform basic operations with Python objects. You also learned more about collections and how to use them to hold and access data. We'll go much deeper into these topics in the coming chapters. It's time to learn with our fingers and do some exercises to deepen our understanding of the basics.

##  Exercises

  1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. For example, if your name is John Doe, you should combine `'John'` and `'Doe'` to get `'John Doe'`.

#### Solution
    
        print('John' + ' ' + 'Doe')   # John Doe
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

Use the REPL and the arithmetic operators to extract the individual digits of `4936`:

    1. One place is `6`. 
    2. Tens place is `3`. 
    3. Hundreds place is `9`. 
    4. Thousands place is `4`. 

Each digit may require multiple Python statements.

Hint 1

It's easier to extract the digits right-to-left rather than left-to-right.

Hint 2

`number % 10` returns the rightmost digit of a number. You can use this repeatedly to extract all of the digits.

Hint 3

Once you have the rightmost digit, how do you remove that digit from the number? If we start with `4936` and extract the `6`, how do we now reduce our number to `493`?

Hint 4

You can remove the rightmost digit by using integer division.

#### Solution
    
        >>> number = 4936
    >>> ones = number % 10
    >>> ones
    6
    
    >>> number = number // 10
    493
    
    >>> tens = number % 10
    >>> tens
    3
    
    >>> number = number // 10
    49
    
    >>> hundreds = number % 10
    >>> hundreds
    9
    
    >>> thousands = number // 10
    >>> thousands
    4
    

Note that you don't need to use `%` for the thousands digit.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. What does the following code do? Why?
    
        print('5' + '10')
    

#### Solution

The code prints `510`. When used with string operands, `+` performs concatenation and returns a new string. We've merely joined `'5'` and `'10'` to produce `'510'`.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Refactor the code from the previous exercise to use coercion to print `15` instead.

#### Solution
    
        print(int('5') + int('10'))
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
    
        foo = ['a', 'b', 'c']
    print(foo[3])      # will this result in an error?
    

#### Solution

Yes, an error will occur: `list index out of range`. When you use an index value with no corresponding element, Python raises an `IndexError` error.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. To what value does the following expression evaluate?
    
        'foo' == 'Foo'
    

#### Solution

It evaluates as `False` since the case matters when comparing strings.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. What will the following code do? Why?
    
        int('3.1415')
    

#### Solution

It raises a `ValueError` since the string value `3.1415` does not represent a valid integer.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. To what value does the following expression evaluate?
    
        '12' < '9'
    

#### Solution

The expression evaluates as `True` since the operands are strings, not numbers. Python performs a character-by-character comparison from left to right when comparing string values. Thus, on the first comparison, it determines that `'1'` < `'9'`, so `'12'` must be less than `'9'`.

If you used numbers instead of strings, the expression would be `False`.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Variables

A fundamental tenet of programming is that programs must store information in memory to use and manipulate it. Variables are the means for doing that in almost all computer languages. They provide a way to label data with a descriptive name that helps us and other readers understand a program. Consider variables as labels that identify particular objects your program creates and uses.

We'll use a few "functions" in this chapter to ensure the code works as intended. Don't worry too much about how functions work. All you need to know for this chapter is:

  * The `def` statement creates a function. 
  * You "call" a function by appending `()` to the function name. 
  * A function can be called multiple times; each call executes the code in the function body. 



We'll learn more about functions later. For now, please don't put too much effort into understanding them.

## Variables and Variable Names

A variable is a label attached to a specific value stored in a program's memory. Typically, variables can be changed; we can connect the variable to a different value somewhere else in memory. For brevity, we often talk of assigning or reassigning an object to a variable. We also speak of variables as containing data, though that's not entirely accurate, as we'll learn later in this book.

Consider this code:
    
    
    answer = 41
    print(answer)       # 41
    
    answer = 42
    print(answer)       # 42
    

When Python sees line 1 of this code, it sets aside a bit of memory and stores the value `41` in that area. It also creates a variable named `answer` that we can use to access that value.

On line 4, we **reassign** the value `42` to the variable named `answer`. That is, Python makes `answer` refer to a new object. In particular, you must understand that we're not changing the object that represents `41` \-- we're assigning an entirely new value to the `answer` variable.

### Variable Naming

> There are two hard problems in computer science: cache invalidation, naming things, and off-by-one errors. _
> 
> \-- Author unknown
> 
> _

Properly naming variables is traditionally viewed as one of the most challenging tasks in computer programming. If you're new to programming, this might seem odd. After all, how tough can it be to choose a name? As it turns out, it is challenging. Consider how much effort many new parents require to select a name for their baby.

A variable name must accurately and concisely describe the variable's data. In large programs, it's challenging to remember what each variable contains. If you use non-descriptive names like `x`, `i`, and `dct`, you may forget what data that variable represents. Other readers -- programmers -- must suss out the meaning for themselves. Therefore, when naming variables, think hard about the names. Ensure they are accurate, descriptive, and understandable to other readers. That might be you when you revisit the program a few months or years later.

Variable names are often referred to by the broader term **identifiers**. In Python, identifiers refer to several things:

  * Variable and constant names 
  * Function and method names 
  * Function and method parameter names 
  * Class and module names 



You'll meet all these things as you move through the Launch School Core curriculum. We'll often use the term _identifier_ when discussing names in general: variables, constants, functions, classes, etc. We'll use one of the more specific terms when we need to limit the scope of a discussion.

## Naming Conventions

Closely related to the stylistic conventions discussed in the Using Python chapter are the Python naming conventions. Names that follow these conventions are **idiomatic**. In contrast, those that do not are **non-idiomatic** (valid but not idiomatic) or illegal (your code will either raise a syntax error or do something unexpected).

  * **Naming conventions for most identifiers (excluding constant and class names)** :

    * Use **snake_case** formatting for these names. 
    * Names may contain lowercase letters (a-z), digits (0-9), and underscores (`_`). 
    * Names should begin with a letter. 
    * If the name has multiple words, separate the words with a single underscore (`_`). 
    * Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used. 
    * Names may only use letters and digits from the standard ASCII character set. 
Idiomatic Names  
---  
`foo`  
`answer_to_ultimate_question`  
`eighty_seven`  
`index_2`  
`index2`  
  * **Constant names (unchanging named values)** :

    * Use **SCREAMING_SNAKE_CASE** formatting for these names. 
    * Names may contain uppercase letters (A-Z), digits (0-9), and underscores (`_`). 
    * Names should begin with a letter. 
    * If the name has multiple words, separate the words with a single underscore (`_`). 
    * Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used. 
    * Names may only use letters and digits from the standard ASCII character set. 
Idiomatic Names  
---  
`FOO`  
`ANSWER_TO_ULTIMATE_QUESTION`  
`EIGHTY_SEVEN`  
`INDEX_2`  
`INDEX2`  
  
The constant naming convention is advisory only. Python has no way to ensure that constants are never changed. Whether a constant ever changes is entirely up to the programmer, not Python.

  * **Class names** :

    * Use **PascalCase** formatting for these names. PascalCase is sometimes called **CamelCase** (with both Cs capitalized). 
    * Names may contain uppercase and lowercase letters (A-Z, a-z) and digits (0-9). 
    * Names should begin with an uppercase letter. 
    * If the name has multiple words, capitalize each word. 
Idiomatic Names  
---  
`Foo`  
`UltimateQuestion`  
`FourLeggedPets`  
`PythonVersion2Rules`  
  
We'll meet a few class names in this book but will leave a full discussion for our Object Oriented Programming in Python book.




Note that many non-idiomatic names are still legal (valid) Python identifiers. Sometimes, it makes sense to break the rules. However, not all identifiers are legal; here are some things you must do:

  * You can use letters, digits, and underscores in Python identifiers. Extended ASCII and Unicode letters and digits are allowed. 
  * You may not use punctuation characters, most special characters, or whitespace. 
  * You may not start identifiers with a digit. 
  * You may not use Python's reserved words such as `if`, `def`, `while`, `return`, and `pass` as names. 

Non-Idiomatic Names | Explanation  
---|---  
fourWayIntersection | camelCase  
Schön | Extended ASCII  
Illegal Names | Explanation  
---|---  
pass | Reserved word  
3xy | Starts with digit  
ultimate-question | Hyphen  
one two three | Whitespace  
is_lowercase? | Punctuation  
is+lowercase | Special character  
  
Most illegal names will raise an error. However, if the illegal name looks like valid Python, you won't get an error:
    
    
    first,last = ['Mary', 'Wonder']
    

That example creates two variables, `first` and `last`, and assigns them to `Mary` and `Wonder`, respectively.

## Creating and Reassigning Variables

We create (**initialize**) most variables by simply giving them a value. That happens as part of an assignment statement:
    
    
    forename = 'Clare'       # initialization (also called assignment)
    

Initializations are also said to provide a **definition** for the variable.

No special keywords are required to define variables. We can also give new values to variables by simply reassigning them:
    
    
    forename = 'Clare'       # initialization (also called assignment)
    # omitted code
    forename = 'Victor'      # reassignment
    

An assignment like `foo = bar` can be described in two main ways:

  1. The variable `foo` is assigned the value of `bar`. 
  2. The value of `bar` is assigned to the variable `foo`. 



If `bar` is a literal value, you can skip mentioning "value of".

Both phrases mean the same thing, but phrase 1 is usually preferred. However, phrase 2 is perfectly acceptable. Think of it like this:

  * Kim has been assigned the task of building safety coordinator. 
  * The task of building safety coordinator has been assigned to Kim. 



Both statements mean the same thing, and so it is with variables and values.

Note that the same phrasing can be used when talking about reassignment: a variable can be reassigned to a new value, or a value can be reassigned to a variable.

At Launch School, we mainly use phrase 1. However, don't be confused if we sometimes use phrase 2. Sometimes, phrase 2 just reads better.

### How Initialization and Reassignment Work

When you initialize a variable, Python gives it an initial value and sticks that value somewhere in the computer's memory. It also allocates a small amount of memory for the variable itself, then places the value's memory address into the variable's spot in memory.

For instance, consider this code:
    
    
    foo = 'abcdefghi'
    

When Python encounters this code, it will create the string `'abcdefghi'` somewhere in memory. Let's assume Python stores the string at memory address 73420. Next, it creates a variable somewhere else in memory. Let's suppose the variable is at address 10230. It then associates address 10230 with the name `foo`. Python stores the address of the string (73420) at address 10230. Thus, we get a situation that looks like this:

![Assigned variables](https://ls-general-public.s3.amazonaws.com/images/python_book/python/images/assigned_variable.png)

Consider what happens when we later run this reassignment:
    
    
    foo = 'Hello'
    

Python creates the new string `'Hello'` somewhere in memory. We can assume that `'Hello'` is stored at memory address 87160. Since we already have a `foo` variable, Python simply replaces the value at address 10230 with 87160. This breaks the connection with the original string and establishes a new one with the new string. Things now look like this:

![Reassigned variables](https://d186loudes4jlv.cloudfront.net/python/images/reassigned_variable.png)

## Creating Constants

Constants are created (initialized) in the same way as variables: by giving them a value. That happens as part of an assignment statement:
    
    
    PINING_FOR = 'fjords'         # initialization
    

As with variable creation, no keywords are required to create constants. However, you should use SCREAMING_SNAKE_CASE in observation of the constant naming convention.

Since constants should be unchanging, you should never reassign a constant.

Constants are usually defined in the global scope. The definitions are usually written at the top of the program file, just below any imports. You can use constants anywhere, but they should be defined globally. Thus, you can use constants in functions, but you shouldn't create a constant inside a function.

**Constants aren't constant in Python**. Python does not support true constants. Instead, the SCREAMING_SNAKE_CASE naming convention is solely for programmers. For instance, the name `FIRST_BASE` meets the naming conventions for constants, so you should think of `FIRST_BASE` as a constant. However, since Python places no constraints on such names, you can easily change the value assigned to `FIRST_BASE`. Changing a constant's value is poor practice and may make you unpopular at work.

## Expressions and Assignment

Assignment and reassignment are often more complex than simply assigning a literal value to a variable. Assignment and reassignment often use expressions on the right side of the `=` to determine the desired value. For instance:
    
    
    left_side = 5
    right_side = 32
    total = left_side + right_side  # total = 37
    print(total)                    # prints 37
    

This code starts with two simple assignments that initialize the `left_side` and `right_side` variables to `5` and `32`, respectively. Next, we add the values of `left_side` and `right_side` together and assign the result to `total`, which we then print.

Here's an example that uses a function call to compute the resulting value for the assignment:
    
    
    def square(number):
        return number * number
    
    forty_two_squared = square(42)
    print(forty_two_squared)                # 1764
    

The expression on the right side of the `=` operator can be any valid expression. It can be as simple or complex as needed, though you should strive to keep them readable and easy to understand.

The variable to the left of the `=` operator is always the target variable for the resulting value. That is, the expression's value will be assigned to the variable.

It's worth noting that the right side of an assignment is always completely evaluated before assigning the result to the variable. That means you can write code like this:
    
    
    foo = 42            # foo is 42
    foo = foo - 2       # foo is now 40
    foo = foo * 3       # foo is now 120
    foo = foo + 5       # foo is now 125
    foo = foo // 25     # foo is now 5
    foo = foo / 2       # foo is now 2.5
    foo = foo**3        # foo is now 15.625
    print(foo)          # prints 15.625
    

In lines 2-7, the right side of each assignment is computed first using whatever value `foo` had most recently. Thus, `foo` was 42 on line 2, 40 on line 3, and so on. On each line, a computation is performed using the current value of `foo`. Python then reassigns the newly computed value to `foo`.

You can also use expressions to initialize constants. However, this is less common than evaluating expressions for a variable.

## Augmented Assignment

The assignments at the end of the previous section all follow a similar pattern: they take the current value of a variable, perform an arithmetic operation on the variable's value, and then reassign the variable to the newly computed value. This sort of operation is so common that most languages have a shorthand notation called **augmented assignment** or **assignment operators** :
    
    
    foo = 42            # foo is 42
    foo -= 2            # foo is now 40
    foo *= 3            # foo is now 120
    foo += 5            # foo is now 125
    foo //= 25          # foo is now 5
    foo /= 2            # foo is now 2.5
    foo **= 3           # foo is now 15.625
    print(foo)          # prints 15.625
    

Each statement is noticeably shorter than the original, but the results are identical. While there's little or no performance benefit to augmented assignment, most developers find the syntax more readable, and you're less likely to misspell one of the variable names.

Augmented assignment also works with string concatenation and repetition. In fact, it works with any type that supports the various operators.
    
    
    bar = 'xyz'          # bar is 'xyz'
    bar += 'abc'         # bar is now 'xyzabc'
    bar *= 2             # bar is now 'xyzabcxyzabc'
    print(bar)           # prints xyzabcxyzabc
    
    
    
    bar = [1, 2, 3]     # bar is [1, 2, 3]
    bar += [4, 5]       # + with lists appends
                        # bar is now [1, 2, 3, 4, 5]
    print(bar)          # prints [1, 2, 3, 4, 5]
    
    
    
    bar = {1, 2, 3}     # bar is {1, 2, 3}
    bar |= {2, 3, 4, 5} # | performs set union
                        # bar is now {1, 2, 3, 4, 5}
    bar -= {2, 4}       # - performs set difference
                        # bar is now {1, 3, 5}
    print(bar)          # prints {1, 3, 5}
    

Augmented assignment also works with constants. However, as with constant reassignment, it is poor practice.

Note that augmented assignment is a statement, not an expression. Thus, you can't use augmented assignment as a function argument or return value:
    
    
    def foo(bar):
        print(bar)
    
    a = 3
    foo(a *= 2)
    #     ^^
    # SyntaxError: invalid syntax
    
    
    
    def foo():
        a = 3
        return a *= 2
    #            ^^
    # SyntaxError: invalid syntax
    

If you study the above examples, you may get the impression that `a += b` is equivalent to `a = a + b`. If the left-side variable (e.g., `a`) is immutable, that's true. However, if `a` is mutable, the expression may not be equivalent to `a = a + b`. For instance, if `a` and `b` are both lists, then `a += b` is actually equivalent to `a.extend(b)`. The resulting values are the same, but we'll see later why this behavior is fundamentally different from `a = a + b`.

## Reassignment vs. Mutation

There are two ways to change things in Python and most other programming languages. You can change the **binding** of the variable by making it reference a new object, or you can change the value of the object assigned (**bound**) to the variable. The former is known as **reassignment** while the latter is known as **mutation**.

A variable is a name that refers to an object at a specific place in memory. Reassignment makes that name refer to a different object somewhere else in memory. Mutation, on the other hand, does not change which object the variable refers to. Instead, it changes the object itself. After mutating an object assigned to a specific variable, the variable continues to refer to the same object (albeit altered) at the same memory location.

This distinction is crucial in any language that permits reassignment and mutation, as it significantly impacts how those languages work. One subtle but important distinction is the difference between reassigning a variable and reassigning an element in a list, dict, or other mutable collection. Reassigning an element of a mutable collection _doesn't reassign the variable_ ; it mutates the collection.

Here are some examples illustrating the differences between reassignment and mutation. Pay close attention, as this is a crucial concept.
    
    
    num = 3               # assignment (initialization)
    my_list = [1, 2, 3]   # assignment (initialization)
    my_dict = {           # assignment (initialization)
        'a': 1,
        'b': 2,
    }
    
    num = 42              # Reassignment
    my_list[1] = 42       # Reassignment of element,
                          # my_list is mutated!
    my_dict['b'] = 3      # Reassignment of dict pair
                          # my_dict is mutated!
    
    # You can still reassign the variables
    my_list = [2, 3, 4]   # Reassignment
    my_dict = { 'x': 0 }  # Reassignment
    

Things get a little fuzzy when using augmented assignment. As mentioned earlier, `a += b` is equivalent to `a = a + b` if `a` is immutable. In that case, then augmented assignment is a form of reassignment.

However, if `a` is mutable, it may be (and frequently is) mutated in augmented assignments. As we mentioned earlier, `a += b` is equivalent to `a.extend(b)` if `a` and `b` are lists. Thus, `a += b` is not reassignment; it is a mutating operation. This distinction becomes crucial when we discuss variables as pointers.

As much as possible, we use the terms mutation or mutate to describe any mutating operation. We'll talk more about these concepts throughout this book and in almost every course at Launch School. For now, keep the distinction between reassignment and mutation in mind.

## Summary

In this chapter, we've learned how to use variables and constants to store information for later use. In particular, we've learned what variables and constants are and how we use and manipulate them. We've also learned how to assign and reassign variables and how to use augmented assignment.

Mutation and reassignment are two more fundamental concepts. Understanding mutation will help you catch, fix, and avoid an entire class of bugs.

Let's apply that knowledge in some exercises.

##  Exercises

  1. Classify the following potential non-constant **variable** names as _idiomatic_ , _non-idiomatic_ , or _illegal_. For the non-idiomatic and illegal names, explain your choice.

Name  
---  
`index`  
`CatName`  
`lazy_dog`  
`quick_Fox`  
`1stCharacter`  
`operand2`  
`BIG_NUMBER`  
`π`  
  
#### Solution

Name | Status | Explanation  
---|---|---  
`index` | Idiomatic |   
`CatName` | Non-idiomatic | Should not use uppercase letters  
`lazy_dog` | Idiomatic |   
`quick_Fox` | Non-idiomatic | Should not use uppercase letters  
`1stCharacter` | Illegal | Should not begin with a digit  
`operand2` | Idiomatic |   
`BIG_NUMBER` | Non-idiomatic | Should not use uppercase letters  
`π` | Non-idiomatic | π is not an ASCII character  
  
**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Classify the following potential **function** names as _idiomatic_ , _non-idiomatic_ , or _illegal_. For the non-idiomatic and illegal names, explain your choice.

Name  
---  
`index`  
`CatName`  
`lazy_dog`  
`quick_Fox`  
`1stCharacter`  
`operand2`  
`BIG_NUMBER`  
`π`  
  
#### Solution

Since function names in Python follow the same conventions as variable names, the answer to this question is the same as the previous question.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Classify the following potential **constant** names as _idiomatic_ , _non-idiomatic_ , or _illegal_. For the non-idiomatic and illegal names, explain your choice.

Name  
---  
`index`  
`CatName`  
`snake_case`  
`LAZY_DOG3`  
`1ST`  
`operand2`  
`BIG_NUMBER`  
`Π`  
  
#### Solution

Name | Status | Explanation  
---|---|---  
`index` | Non-idiomatic | Should not use lowercase letters  
`CatName` | Non-idiomatic | Should not use lowercase letters  
`snake_case` | Non-idiomatic | Should not use lowercase letters  
`LAZY_DOG3` | Idiomatic |   
`1ST` | Illegal | Should not begin with a digit  
`operand2` | Non-idiomatic | Should not use lowercase letters  
`BIG_NUMBER` | Idiomatic |   
`Π` | Non-idiomatic | Π is not an ASCII character  
  
**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Classify the following potential **class** names as _idiomatic_ , _non-idiomatic_ , or _illegal_. For the non-idiomatic and illegal names, explain your choice.

Name  
---  
`index`  
`CatName`  
`Lazy_Dog`  
`1ST`  
`operand2`  
`BigNumber3`  
`Πi`  
  
#### Solution

Name | Status | Explanation  
---|---|---  
`index` | Non-idiomatic | Should not begin with a lowercase letter  
`CatName` | Idiomatic |   
`Lazy_Dog` | Non-idiomatic | Should not use underscores  
`1ST` | Illegal | Should not begin with a digit  
`operand2` | Non-idiomatic | Should not begin with a lowercase letter  
`BigNumber3` | Idiomatic |   
`Πi` | Non-idiomatic | Π is not an ASCII character  
  
**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. Write a program named `greeter.py` that greets `'Victor'` three times. Your program should use a variable and not hard code the string value `'Victor'` in each greeting. Here's an example run of the program:
    
        $ python greeter.py
    Good Morning, Victor.
    Good Afternoon, Victor.
    Good Evening, Victor.
    

#### Solution
    
        # This solution uses concatenation
    name = 'Victor'
    print('Good Morning, ' + name + '.')
    print('Good Afternoon, ' + name + '.')
    print('Good Evening, ' + name + '.')
    
    
        # This solution uses f-string interpolation
    name = 'Victor'
    print(f'Good Morning, {name}.')
    print(f'Good Afternoon, {name}.')
    print(f'Good Evening, {name}.')
    

First, we create a variable that holds the value `'Victor'`. With a variable, we don't need to hard code `'Victor'` each time we greet him. Instead, we can use the variable as part of an expression. In our first solution, we use string concatenation; in the second, we use f-string interpolation.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. Write a program named `age.py` that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.
    
        You are 22 years old.
    In 10 years, you will be 32 years old.
    In 20 years, you will be 42 years old.
    In 30 years, you will be 52 years old.
    In 40 years, you will be 62 years old.
    

#### Solution
    
        age = 22
    print(f'You are {age} years old.')
    print(f'In 10 years, you will be {age + 10} years old.')
    print(f'In 20 years, you will be {age + 20} years old.')
    print(f'In 30 years, you will be {age + 30} years old.')
    print(f'In 40 years, you will be {age + 40} years old.')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. What happens when you run the following code? Why?
    
        NAME = 'Victor'
    print('Good Morning, ' + NAME)
    print('Good Afternoon, ' + NAME)
    print('Good Evening, ' + NAME)
    
    NAME = 'Nina'
    print('Good Morning, ' + NAME)
    print('Good Afternoon, ' + NAME)
    print('Good Evening, ' + NAME)
    

#### Solution

The program first greets Victor 3 times. It then greets Nina 3 times.

Unfortunately, Python doesn't have real constants. There's no way to prevent the reassignment of `NAME`. If this faux-constant really needs to be changed, you should use a regular variable instead:
    
        name = 'Victor'
    print('Good Morning, ' + name)
    print('Good Afternoon, ' + name)
    print('Good Evening, ' + name)
    
    name = 'Nina'
    print('Good Morning, ' + name)
    print('Good Afternoon, ' + name)
    print('Good Evening, ' + name)
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. **Challenge** : This program uses a bit of math. Don't let that scare you away -- try it anyway.

Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named `balance` that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set `balance` to the correct value.

#### Solution
    
        balance = (1000.00 * 1.05 * 1.05 * 1.05
                       * 1.05 * 1.05)
    print(balance)
    

The program prints `1276.2815625000003` as the final balance. That's not precisely correct. The actual value should be `1276.2815625`. That's close enough when you consider the imprecision of using floats.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  9. Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.

#### Solution
    
        balance = 1000.00
    balance *= 1.05
    balance *= 1.05
    balance *= 1.05
    balance *= 1.05
    balance *= 1.05
    print(balance)
    

This program also prints `1276.2815625000003` as the final balance. Once again, that's close enough.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  10. Assume that `obj` already has a value of `42` when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that `obj` references? Which statements do neither? If necessary, you can read the documentation.
    
        obj = 'ABcd'
    obj.upper()
    obj = obj.lower()
    print(len(obj))
    obj = list(obj)
    obj.pop()
    obj[2] = 'X'
    obj.sort()
    set(obj)
    obj = tuple(obj)
    

#### Solution

The comments in the following code show whether reassignment, mutation, or neither took place on each line of code:
    
        obj = 'ABcd'      # Reassignment
    obj.upper()       # Neither
    obj = obj.lower() # Reassignment
    print(len(obj))   # Neither
    obj = list(obj)   # Reassignment
    obj.pop()         # Mutation
    obj[2] = 'X'      # Mutation
    obj.sort()        # Mutation
    set(obj)          # Neither
    obj = tuple(obj)  # Reassignment
    

A simple assignment like `var = something` is always either an initialization or a reassignment. Since `obj` has already been initialized (it has a value of `42` before this code was reached), lines 1, 3, 5, and 10 perform reassignment. In a few situations, mutation and reassignment can happen in the same statement. None of the above statements do both.

`obj.upper` does not mutate the caller, so line 2 does neither. Likewise, since `print`, `len`, and `set` don't mutate their arguments, lines 4 and 9 are neither.

The remaining statements all mutate the object referenced by `obj`. `pop` removes the last element of the list. `obj[2] = 'X'` reassigns the element at index 2, but it mutates `obj` itself. Finally, `sort` mutates the object when it performs an in-place sort.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Input/Output

Computers and software don't live in isolation. They are tools that solve real-world problems, meaning they must interact with the real world. A computer needs to take input from some source, perform some actions on that input, and then provide output.

Computer programs can use many input sources, such as mice, keyboards, disks, the network, and environmental sensors. Similarly, a program can write output to multiple places, such as the screen, a log, or a network.

A computer can obtain input from another computer's output. For example, when you enter your login credentials for a website, your computer first encrypts them. It then sends them to the website's authentication server, which accepts (inputs) the data and attempts to verify your identity. In this fashion, two computers can perform different parts of a common task.

In this chapter, we'll discuss the most basic techniques a program can use to interact with the outside world: reading keyboard input and displaying output in a terminal.

## Terminal Output

You've already seen one way to display output in the terminal: the `print` function. This built-in function takes any Python value, regardless of type, and prints it. Let's see an example. Create a file named `greetings.py` with the following content:
    
    
    name = 'Jane'
    print(f'Good morning, {name}!')
    

In this simple example, we initialize a `name` variable with the string `'Jane'`, then use it in an f-string interpolation to build and display a greeting message. Run the program to see it in action:
    
    
    $ python greetings.py
    Good morning, Jane!
    

The `print()` function works with all data types, often -- but not always -- formatting the output in some manner that makes it somewhat understandable to humans. For instance:
    
    
    >>> print({ 'a': 1, "b": 42, 'c': "string",
    ...         'd': [5, 6], 'e': { 8, 9, 10 }})
    # Pretty printed for clarity
    {
        'a': 1,
        'b': 42,
        'c': 'string',
        'd': [5, 6],
        'e': {8, 9, 10}
    }
    
    >>> import time
    >>> print(time.asctime())
    Mon Aug 21 22:59:29 2023
    

You can print multiple objects by just listing them one after the other as arguments to `print()`:
    
    
    >>> print(1, 2, 3, 'a', 'b')
    1 2 3 a b
    
    >>> print([1, 2, 3], 4, False, { 5, 6, 7, 8})
    [1, 2, 3] 4 False {8, 5, 6, 7}
    

By default, multiple items are separated by spaces. You can use a different separator with the `sep` keyword argument (we discuss keyword arguments in the Core Curriculum):
    
    
    print(1, 2, 3, 'a', 'b', sep=',')      # 1,2,3,a,b
    print('a', 'b', 'c', 'd', 'e', sep='') # abcde
    

Note that using an empty string as the `sep` value causes all the values to be printed without separation.

The `end` keyword argument defines what `print()` prints after it prints the last argument. By default, it prints a newline (`\n`). The most common reasons for using `end` are compatibility with Windows (which sometimes needs a newline of `\r\n`) and for suppressing the newline altogether. Here are two more examples:
    
    
    >>> print(1, 2, 'a', 'b', sep=',', end=' <-\n')
    1,2,a,b <-
    
    >>> print('a', 'b', end='', sep=','); print('c', 'd', sep=',')
    a,bc,d
    

Note the semicolon (`;`) on line 4: that's an easy way to enter multiple statements on a single line. Mostly, you should only use semicolons like this in the REPL.

Finally, to start a new line immediately without printing anything else, just run `print()` with no arguments:
    
    
    >>> print()
    
    >>>
    

## Terminal Input

In the previous example, we assigned a value to `name` and displayed a fixed greeting message that uses that name. That's probably not the most exciting thing you've seen today. We **hard-coded** the name, which means the program will always use the same name. We must modify and rerun the program to greet a different person. You probably wouldn't bother using a program that worked like that.

Can we ask the user to provide her name and greet her with a message that uses the name she entered? Yes, we can. Python has a built-in function called `input()` that lets Python programs read input from the terminal.

### Example: Greet the User By Name

Let's use `input()` to write a program that displays a personalized greeting message for the user based on the name she provides. Create a file named `personalized_greeting.py` with the following code:
    
    
    print("What's your name?")
    name = input()
    
    print(f'Good Morning, {name}!')
    

Run the program from the command line. It displays the `What's your name?` question, then waits for your input. When you enter a name and hit Return, the program displays a custom greeting message:
    
    
    $ python personalized_greeting.py
    What's your name?
    Rachele
    Good Morning, Rachele!
    

You can also use the `input()` function to display the prompt the user sees:
    
    
    # highlight
    name = input("What's your name? ")
    # endhighlight
    
    print(f'Good Morning, {name}!')
    

Note the space after the `?`: you'll see why that's needed when you run the program:
    
    
    $ python personalized_greeting.py
    What's your name? Rachele
    Good Morning, Rachele!
    

See how `input()` retrieved the input from the same line as the prompt? That's why we needed the extra space. Without the space, we'd see:
    
    
    What's your name?Rachele
    Good Morning, Rachele!
    

Alternatively, we can have `input()` output a newline instead of a space:
    
    
    # highlight
    name = input("What's your name?\n")
    # endhighlight
    
    print(f'Good Morning, {name}!')
    
    
    
    $ python personalized_greeting.py
    What's your name?
    Rachele
    Good Morning, Rachele!
    

That's more like what we started with when we used `print()` to display the prompt. In this code, the `\n` is an escape character that the computer treats as a newline. `\n` is accepted almost universally in programming languages, though the circumstances needed to produce the desired effect may vary slightly.

### Add Two Numbers

Let's write a program that asks for two numbers from the user, adds them, and then displays the result. Put the following code in a new file called `sum_numbers.py` and then run it:
    
    
    number1 = input('Enter the first number: ')
    number2 = input('Enter the second number: ')
    sum = number1 + number2
    
    print(f'The numbers {number1} and {number2} '
          f'add to {sum}')
    
    
    
    $ python sum_numbers.py
    Enter the first number: 2
    Enter the second number: 3
    The numbers 2 and 3 add to 23
    

Oops. Something isn't right. The program reports that the result is `23`, not `5` like we want. Where do you think the problem lies? If you said that `input()` returns strings, so `+` performs concatenation, you're right! Since `number1` and `number2` both hold string values instead of numbers, the `+` operator concatenates them instead of adding them. If you want to add two variables arithmetically, both must have a numeric data type.

As we learned earlier, we can convert (coerce) strings to numbers with the `int()` or `float()` function. Update line 3 from `sum_numbers.py` to match this code:
    
    
    number1 = input('Enter the first number: ')
    number2 = input('Enter the second number: ')
    # highlight
    sum = float(number1) + float(number2)
    # endhighlight
    
    print(f'The numbers {number1} and {number2} add to {sum}')
    
    
    
    $ python sum_numbers.py
    Enter the first number: 2
    Enter the second number: 3
    The numbers 2 and 3 add to 5.0
    

`input()` still returns a string, but we've coerced each string to a float this time. With numbers on both sides of the `+`, Python adds them arithmetically.

Be sure to play with these examples a bit. You can, for example, replace addition with subtraction or multiplication in the above example. Try to think of some applications of `input()` on your own.

I/O (Input/Output) in Python is a complex topic requiring knowledge of concepts we haven't yet learned. They're essential concepts, but we don't discuss them in this book; we cover them in the Core Curriculum. Until then, we can use `print()` and `input()` to interact with users.

## Summary

These examples are simple, but they demonstrate how you can obtain user input, perform some work with that input, and then use the results to show some output to the user. This input/output cycle is at the heart of every computer program. After all, software that accepts no input and provides no output is useless.

##  Exercises

  1. Write a program named `greeter.py`. The program should ask for your name, then output `Hello, NAME!` where `NAME` is the name you entered:
    
        $ python greeter.py
    What is your name? Sue
    Hello, Sue!
    

#### Solution
    
        name = input('What is your name? ')
    print('Hello, ' + name + '!')
    
    
        name = input('What is your name? ')
    print(f'Hello, {name}!')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Modify the `greeter.py` program to ask for the user's first and last names separately, then greet the user with their full name.
    
        $ python greeter.py
    What is your first name? Bob
    What is your last name? Roberts
    Hello, Bob Roberts!
    

#### Solution
    
        first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    print(f'Hello, {first_name} {last_name}!')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Write a program named `age.py` that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.
    
        How old are you? 27
    
    You are 27 years old.
    In 10 years, you will be 37 years old.
    In 20 years, you will be 47 years old.
    In 30 years, you will be 57 years old.
    In 40 years, you will be 67 years old.
    

#### Solution
    
        # This solution coerces the input age when a numeric
    # age is needed. This code is repetitive.
    
    age = input('How old are you? ')
    print()
    print(f'You are {age} years old.')
    print(f'In 10 years, you will be {int(age) + 10} years old.')
    print(f'In 20 years, you will be {int(age) + 20} years old.')
    print(f'In 30 years, you will be {int(age) + 30} years old.')
    print(f'In 40 years, you will be {int(age) + 40} years old.')
    
    
        # This solution reduces the repetition by calling int
    # once only.
    
    age = int(input('How old are you? '))
    print()
    print(f'You are {age} years old.')
    print(f'In 10 years, you will be {age + 10} years old.')
    print(f'In 20 years, you will be {age + 20} years old.')
    print(f'In 30 years, you will be {age + 30} years old.')
    print(f'In 40 years, you will be {age + 40} years old.')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)
# Functions and Methods

As a programmer, you often need a chunk of code in two or more program locations. No matter how often you want to use that code, you don't want to write that code repeatedly. What can you do?

Sometimes, you may realize that you have some code that would be perfect for use in another program. Can you somehow reuse that code without copying and pasting it?

You may sometimes find yourself with some complicated code that has become hard to read, understand, and maintain. What can you do to improve matters?

Most languages support the concept of **procedures** , blocks of code that run as separate units. In Python, we call these **functions** or **methods**.

Functions help solve all of these problems. They help reduce repetitive code, enable easy code reuse, and improve code readability and maintainability. Methods provide the same benefits as functions, but their behaviors are limited to specific objects.

## Calling Functions

Using a function means **calling** , **invoking** , **executing** , or **running** it. All of those terms mean the same thing. When Python encounters a function call, it transfers program flow to the code that comprises the function and executes that code. When the code finishes its work, the function **returns** a value to the code that invoked it. The calling code is free to use or ignore the return value as the programmer sees fit. Execution resumes from where the function was called.

To invoke a function, write the function's name followed by a pair of parentheses `()`. For example, when we call the `hello` function in the following code, we write `hello()`:
    
    
    def hello():
        print('Hello')
        return True
    
    hello()         # invoking function; ignore return value
    print(hello())  # using return value in a `print` call
    

The first 3 lines of this program contain the **function definition** or **function declaration**. We'll come back to function definitions a little later in this chapter. For now, notice that the function returns the value `True` when it is done running.

Lines 5 and 6 show two calls to the `hello` function. In the first invocation, we ignore the return value. In the second, we capture the return value and pass it to the `print` function for printing.

What does the `print` function return? That's easy to check:
    
    
    >>> print(print())
    None
    

We'll see why that is later.

Functions can also take one or more comma-separated **arguments** between the parentheses. Functions usually use arguments to modify the actions they take. A single argument is passed to the `print` function on lines 2 and 6 above. In this case, it tells `print` what to print.

To provide additional arguments, separate them with commas:
    
    
    print('hello', 'good-bye', 'farewell')
    

If you have a lot of arguments (or some longish ones), you can spread them over several lines:
    
    
    print(
        'hello',
        'good-bye',
        'farewell',
        'adios',
        'ciao',
        'auf wiedersehen',
    )
    

## Built-in Functions

Built-in functions are functions that are always available in Python. Many of these functions are used in almost every significant Python program. For instance, you should already be comfortable with the `print` function.

As of Python 3.11.4, there are approximately 70 built-in functions. We've already met a number of these:

  * `float`, `int`
  * `str`, `list`, `tuple`
  * `set`, `frozenset`
  * `input`, `print`
  * `type`
  * `len`



You can learn more in the [Python documentation for Built-in Functions](https://docs.python.org/3/library/functions.html). Let's look at a few of these functions (we'll meet even more in the Core Curriculum).

###  `min` and `max`

You can use the `min` and `max` functions to determine a collection's minimum and maximum values. The collection's objects must have an ordering that recognizes the `<` and `>` operators for comparing any pair of those objects.
    
    
    print(min(-10, 5, 12, 0, -20))      # -20
    print(max(-10, 5, 12, 0, -20))      # 12
    
    print(min('over', 'the', 'moon'))   # 'moon'
    print(max('over', 'the', 'moon'))   # 'the'
    
    print(max(-10, '5', '12', '0', -20))
    # TypeError: '>' not supported between instances
    # of 'str' and 'int'
    

You can also use `max` and `min` with a single iterable argument, such as a list, set, or tuple:
    
    
    my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
                'puddy', 'tat')
    print(min(my_tuple)) # 'a'
    print(max(my_tuple)) # 'tawt'
    

We'll discuss iterables in a later chapter. For now, you only need to know that strings, sequences, mappings, and sets are iterable.

###  `ord` and `chr`

Given a single character, `ord` returns an integer that represents the Unicode code point of that character. For the standard ASCII character sets, the code points refer to the values of the characters in the [standard ASCII character set](https://www.ascii-code.com/ASCII). For example:
    
    
    print(ord('a'))               # 97
    print(ord('A'))               # 65
    print(ord('='))               # 61
    print(ord('~'))               # 126
    

`chr` is the inverse of `ord`. That is, it converts an integer to the corresponding Unicode character:
    
    
    print(chr(97))                # a
    print(chr(65))                # A
    print(chr(61))                # =
    print(chr(126))               # ~
    

### Truthy and Falsy

In the remainder of this assignment, we will use the terms **truthy** and **falsy** to describe values. These are not the same thing as `True` and `False`, but are a little more general. The following values are said to be falsy:

  * `False`, `None`
  * all numeric `0` values (integers, floats, complex) 
  * empty strings: `''`
  * empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`
  * Custom data types can also define additional falsy value(s). 



All other values are said to be truthy.

We will revisit this concept in more detail in the next chapter. For now, you only need to be aware of the concept. You can think of truthy and falsy as `True` and `False` for now.

###  `any` and `all`

Two very useful built-in functions are the `any` and `all` functions. They both operate on iterable collections, such as lists, tuples, ranges, dictionaries, and sets.

The `any` function returns `True` if any element in a collection is truthy, `False` if all of the elements are falsy. On the other hand, `all` returns `True` if all of the elements are truthy, `False` otherwise.
    
    
    collection1 = [False, False, False]
    collection2 = (False, True, False)
    collection3 = {True, True, True}
    
    print(any(collection1))       # False
    print(any(collection2))       # True
    print(any(collection3))       # True
    print(any([]))                # False
    
    print(all(collection1))       # False
    print(all(collection2))       # False
    print(all(collection3))       # True
    print(all([]))                # True
    

Notice that `any` returns `False` for an empty collection since none of the elements are truthy. However, `all` returns `True` for the same collection since none of the elements are falsy (all of the elements are thus truthy).

This example may not seem very useful. However, if you have a collection of something other than Booleans, you can use a comprehension with `any` or `all` to test whether any or all of the elements meet a certain condition. (We'll meet comprehensions a little later.)

For instance, assume you want to determine whether a list of numbers has any even values in it. You can use a list comprehension to determine which values are even or odd:
    
    
    numbers = [2, 5, 8, 10, 13]
    print([number % 2 == 0 for number in numbers])
    # [True False True True False]
    

You can take that one step further to determine whether any or all of the numbers are even:
    
    
    numbers = [2, 5, 8, 10, 13]
    print(any([number % 2 == 0 for number in numbers])) # True
    print(all([number % 2 == 0 for number in numbers])) # False
    
    numbers = [5, 13]
    print(any([number % 2 == 0 for number in numbers])) # False
    print(all([number % 2 == 0 for number in numbers])) # False
    
    numbers = [2, 8, 10]
    print(any([number % 2 == 0 for number in numbers])) # True
    print(all([number % 2 == 0 for number in numbers])) # True
    

### Functions for the REPL

Some functions are intended for use in a REPL. These functions provide quick access to information about your program or Python itself.

#### The id Function

The `id` function returns an integer that serves as an object's **identity**. Every object has a unique identity that does not change during the object's lifetime. (The identity may be reused later in the program if the original object is discarded.)

In most cases, two instances of an object with the same value will always have two distinct identities. This is not always true, though. For instance, in a process called **interning** , every unique integer object from -5 through 256 has the same identity. Interning also applies to some strings:
    
    
    # Paste this code into the Python REPL
    # Don't run it as a program
    
    s = 'Hello, world!'
    t = 'Hello, world!'
    print(id(s) == id(t))         # False
    
    s = 'supercalifragilisticexpialidocious'
    t = 'supercalifragilisticexpialidocious'
    print(id(s) == id(t))         # True
    
    x = 5
    y = 5
    print(id(x) == id(y))         # True
    
    x = 5
    y = 6
    print(id(x) == id(y))         # False
    

Interning yields memory space savings and performance improvements. We discuss it mainly because new Python programmers sometimes discover this behavior and think they've found a bug. In practice, it's not an important concept, but it's worth being aware of.

By the way: the reason we asked you to paste that code into the Python REPL is that Python interns different things when you run a program file. In the above code, the first `print` will output `True` if you run it as a program.

Later on, we'll see why `id` is useful.

Interning is an implementation detail that varies based on the flavor and version of Python you are using. While most flavors and versions intern the small integers shown above, some intern other values such as certain strings.

Python "flavors" are different implementations of Python. The flavor you are most likely using is CPython, but other flavors include Jython, PyPy, AnacondaPython, and more.

#### The dir Function

When used without arguments, the `dir` function returns a list of all identifiers in the current local scope. When used with an argument, `dir()` returns a list of the object's attributes (typically, the object's methods and instance variables).
    
    
    >>> dir()
    ['__builtins__', '__name__', 'struct']
    
    >>> dir(5)
    ['__abs__', '__add__', '__and__', '__bool__',
        ... a bunch of stuff omitted ...,
     '__xor__', 'as_integer_ratio', 'bit_count',
     'bit_length', 'conjugate', 'denominator',
     'from_bytes', 'imag', 'numerator', 'real',
     'to_bytes']
    

Many of the names shown by `dir` begin and end with two underscores. These are names for the so-called **dunder** (double-underscore) or **magic methods** and **magic variables**. We'll encounter some of these in the [Object Oriented Programming book](/books/oo_python/).

**Helpful Hint** : Use the `sorted` function with the output of `dir`:
    
    
    >>> sorted(dir(range(1)))
    ['__bool__', '__class__', '__contains__',
     '__delattr__', '__dir__', '__doc__', '__eq__',
        ... a bunch of stuff omitted ...,
     'count', 'index', 'start', 'step', 'stop']
    

**Another Helpful Hint** : Use pretty print to print the output in an easier to read format:
    
    
    >>> from pprint import pp
    >>> names = sorted(dir(range(1)))
    >>> pp(names)
    ['__bool__',
     '__class__',
     '__contains__',
     '__delattr__',
     ... a bunch of stuff omitted ...,
     'count',
     'index',
     'start',
     'step',
     'stop']
    

**Yet Another Helpful Hint** : Use a comprehension to limit the output to just the names that don't contain `__`.
    
    
    >>> names = sorted(dir(range(1)))
    >>> names = [name for name in names
    ...          if '__' not in name]
    >>> print(names)
    ['count', 'index', 'start', 'step', 'stop']
    

#### The help Function

When used without arguments, the `help` function prints some basic help on how to use `help`, then leaves you in a special help mode that uses a `help>` prompt.
    
    
    >>> help()
    
    Welcome to Python 3.11's help utility!
    
    If this is your first time using Python, you should definitely check out
    the tutorial on the internet at https://docs.python.org/3.11/tutorial/.
    
    Enter the name ...
       <omitted text>
    
    help>
    

From the `help>` prompt, you can request help on module names, Python keywords, built-in functions, class names, etc. Type the appropriate words at the `help>` prompt and press {Return} or {Enter}.

Quitting the help system may involve two separate steps. If you are currently reading a long help item (such as the help for `str`), you may need to press `q` to terminate the output. After terminating the output, you may need to type another `q` and then press {Return} or {Enter} to exit from the `help>` prompt.

As of Python 3.13.0, you no longer need to use write `help()` to access the help system. You can, instead, just write `help`. When supplying an argument to `help`, you still need to use the parentheses.

You can also request help more directly by placing an appropriate identifier between the parentheses:
    
    
    >>> help(ord)
    Help on built-in function ord in module builtins:
    
    ord(c, /)
        Return the Unicode code point for a one-character string.
    
    >>> help(bool)
    Help on class bool in module builtins:
    
    class bool(int)
     |  bool(x) -> bool
     |
     |  Returns True when the argument x is true, False otherwise.
     |  The builtins True and False are the only two instances of the class bool.
     |  The class bool is a subclass of the class int, and cannot be subclassed.
     |
     |  Method resolution order:
     |      bool
     |      int
     |      object
    
       <omitted text>
    
    >>> help('topics')
    
    Here is a list of available topics. Enter any topic name to get more help.
    
    ASSERTION           DELETION            LOOPING             SHIFTING
    ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
    ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
    ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
    AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
       <omitted text>
    
    >>> help('BOOLEAN')
    Boolean operations
    ******************
    
       or_test  ::= and_test | or_test "or" and_test
       and_test ::= not_test | and_test "and" not_test
       not_test ::= comparison | "not" not_test
    
    In the context of Boolean operations, and also when expressions are
    used by control flow statements...
    
       <omitted text>
    

## Creating Functions

Unless a function is built-in or provided by an imported module, you must create it. A typical function definition (a.k.a., function declaration) looks like this:
    
    
    def func_name():
        func_body
    

Here, we're assigning the function to `func_name`, and `func_body` is some code that performs the function's required action(s).

Here's a function named `say` that prints `Hi!`:
    
    
    def say():
        print('Hi!')
    

Why do we want a function named `say`? To say something, of course! Let's try it. First, we'll create a file named `say.py`, then place the following code inside the file.
    
    
    def say():
        print('Output from say')
    
    print('First')
    say()
    print('Last')
    

Save the file and run it from the terminal:
    
    
    $ python say.py
    First
    Output from say
    Last
    

On line 5 of `say.py`, the code `say()` is a **function call** to the `say` function. When Python runs this program, it creates a function named `say` whose body causes Python to print the text `Output from say` when the function executes. However, that doesn't happen immediately.

On line 4, we use `print` to display `First` on the terminal. On line 5, we **call the function** `say` by appending a pair of parentheses -- `()` \-- to the function's name. This causes Python to temporarily jump into the function's body, which prints the text `Output from say`. Finally, Python returns to the code that immediately follows the call to `say` and prints `Last`.

Note that the parentheses on line 5 -- `()` \-- make this code a function call. Without the parentheses, `say` doesn't do anything useful. It's the function's name, not an invocation. Forgetting the parentheses is usually a bug that can be tough to find since the code may run long after the line with the error. It just won't work. We'll learn about function objects later in the Core Curriculum.

Python programmers often add a triple-quoted string at the beginning of a function's block. This string is a documentation comment -- a **docstring** \-- that Python can access with its `help()` function and the `__doc__` property. It has no effect on your code unless your program is somehow interested in the comments (which can happen):
    
    
    def say():
        """
        The say function prints "Hi!"
        """
        print('Hi!')
    
    print('-' * 60)
    print(say.__doc__)
    print('-' * 60)
    help(say)
    
    
    
    ------------------------------------------------------------
    
        The say function prints "Hi!"
    
    ------------------------------------------------------------
    Help on function say in module \_\_main\_\_:
    
    say()
        The say function prints "Hi!"
    

We won't follow this convention at Launch School, but you should learn to recognize it. You will likely encounter it elsewhere.

## Scope

The **scope** of an identifier determines where you can use it. Python determines scope by looking at where you initialize the identifier. In Python, identifiers have **function scope**. That means that anything initialized inside a function is only available within the body of that function and any nested functions. No code outside of the function body can access that identifier.

Consider this code:
    
    
    def well_howdy(who):
        greeting = 'Howdy'
        print(f'{greeting}, {who}')
    
    well_howdy('Angie')
    print(greeting)
    

In this code, we have a `greeting` variable in the body of `well_howdy`. When we call the function, `Howdy` is assigned to `greeting`, and a more complete greeting message is printed.

When the function is done running, we try to print the value of the `greeting` variable. However, instead of seeing `Howdy`, we get an error message instead:
    
    
    NameError: name 'greeting' is not defined
    

The error occurs since the `greeting` variable is only available inside the `well_howdy` function. The surrounding code has no way to access the variable.

What happens if we define our own `greeting` variable in the outer scope?
    
    
    greeting = 'Salutations'
    
    def well_howdy(who):
        greeting = 'Howdy'
        print(f'{greeting}, {who}')
    
    well_howdy('Angie')
    print(greeting)
    

This time, the code prints `Salutations` on line 8, thus showing that `greeting` is in scope on line 8. However, the outer `greeting` variable plays no part in the function's body. The assignment on line 4 hides the `greeting` variable from line 1. We call this **variable shadowing**.

Let's remove the assignment on line 4 and see what happens:
    
    
    greeting = 'Salutations'
    
    def well_howdy(who):
        print(f'{greeting}, {who}')
    
    well_howdy('Angie')
    print(greeting)
    

This time, we get:
    
    
    Salutations, Angie
    Salutations
    

The key difference here is that we are no longer assigning the `greeting` variable in this function. Instead, we're just accessing its current value. It's the assignment in the first example in this section that causes Python to create a new local variable named `greeting`. Without any assignments in the function body, Python looks for `greeting` in the **lexical scope** , which means it searches the outer scopes for the nearest definition of `greeting`. In this example, the only outer scope of concern is the topmost scope, i.e., the global scope.

If you're familiar with some other programming languages, the following example may be a little surprising:
    
    
    def scope_test():
        if True:
            foo = 'Hello'
        else:
            bar = 'Goodbye'
    
        print(foo)
        print(bar)
    
    scope_test()
    
    
    
    Hello
    UnboundLocalError: cannot access local variable
    'bar' where it is not associated with a value
    

In some languages, the corresponding print code may treat both `foo` and `bar` as out of scope. Both names may be in scope in other languages, but one will have a default value such as `nil` or `undefined`. In still other languages, only one name is in scope. Python comes closest to this last approach, but both names are technically in scope. However, since the `else` block never runs, `bar` is left unassigned. Thus, we get the `UnboundLocalError` message when we try to print it.

As you might expect, constants have the same scoping behavior as variables. In fact, so do function, parameter, class, and module names. Method names act a little differently, but that's a topic for another time.

## Namespaces

Closely related to the concept of scope is the concept of a **namespace**. In Python, a namespace is defined as a mapping of identifiers to objects. In essence, namespaces define the scopes in which Python will look for identifiers. When you refer to an identifier, Python first looks for the identifier in the **local namespace**. That is, it looks in the local scope. If the identifier is not found in the local namespace, Python next looks in any **enclosing namespaces** , i.e., the outer scopes (but not including the global scope). Next, it searches the **global namespace** , which is equivalent to the global scope, and, finally, the **built-in namespace**.

We will not often refer to namespaces at Launch School, but you may encounter the term when looking at other material.

## Arguments & Parameters

Create a new file named `say2.py` with the following code:
    
    
    print('hello')
    print('hi')
    print('how do you do')
    print('Quite all right')
    

Go ahead and run it if you want. Notice how we've duplicated the `print` call several times. Instead of calling it every time we want to output something, we want to have code we can call when we need to print something.

Now, let's update `say2.py` as follows:
    
    
    def say(text):
        print(text)
    
    say('hello')
    say('hi')
    say('how do you do')
    say('Quite all right')
    

At first glance, this program seems silly. It doesn't reduce the amount of code. In fact, it adds more. Also, the `say` function doesn't provide any functionality that `print` doesn't already offer. However, there is a benefit here. We've extracted the logic for displaying text in a way that makes our program more flexible. If we need to change the output style, we can change it in one place: the `say` function. We don't have to change any other code to get the updated behavior. We'll see such an update in a few minutes.

As we saw earlier, we invoke functions by typing their name and a pair of parentheses. `say2.py` illustrates how we define and call a function that takes a value known as an **argument**. Arguments let you pass data from outside the function's scope into the function so it can access that data. You don't need arguments when the function doesn't need access to outside data.

In `say2.py`, the function definition includes `(text)` after the function name. This syntax tells us that we should supply (pass) a single argument to the function when we call it. We include an argument between the invocation parentheses to pass it to `say`. Thus, `say('hello')` passes the argument `'hello'` to the function. We assign the argument's value to the `text` parameter inside `say`.

The names between parentheses in the function _definition_ are called **parameters**. You can think of parameters as placeholders for potential arguments, while arguments are the values assigned to those placeholders.

**Function names and parameters are both considered variable names in Python.** Parameters, in particular, are **local variables**. They are defined locally within the function's body. A function's name is global or local, depending on whether it is at the program's top level or nested inside a class, module, or another function. We'll see several exercises about these issues below; they are essential even if there isn't much to say about them.

Since parameters are merely placeholders, we typically talk of them as **declarations** : they are being used to introduce those names as local variables into a function, but don't obviously provide an immediate value until the function is called. That is, they simply declare variable names.

Arguments are objects passed to a function during invocation. Parameters are placeholders for the objects that will be passed to the function when it is invoked.

Many developers conflate the terms "parameter" and "argument" and use them interchangeably. The difference is typically not crucial to understanding, but using correct terminology is a good idea. **We expect you to do so on Launch School assessments.** Parameters are not arguments. Arguments are not parameters.

You can name functions and parameters with any valid variable name. However, you should use meaningful, explicit names that follow the same naming conventions discussed in the [Variables chapter](/books/python/read/variables). In the above example, we name the parameter `text` since the `say` function expects the caller to pass in some text. Other suitable names might be `sentence` or `message`.

When we call the `say` function, we should provide a value -- the argument -- to assign to the `text` parameter. For instance, on line 4 of `say2.py`, we pass the value `'hello'` to the function, which it uses to initialize `text`. The function can use the value in any way it requires by referencing the parameter name. It can even ignore the argument entirely.

Remember: a parameter's scope is the function where the parameter is used. Thus, the scope of the `text` parameter in `say2.py` is the `say` function. You can't reference the parameter outside of the function's body.

You can define functions that take any number of parameters and accept any number of arguments. For instance, the `add` function defined below takes two parameters, and we invoke it with 2 arguments:
    
    
    def add(left, right):
        sum = left + right
        return sum
    
    sum = add(3, 6)
    

In the above code, `left` and `right` are parameters on line 1. On line 2, however, they are local variables that contain the argument values passed to `add` on line 5.

Python will raise an error if you pass too many or too few arguments to a function. However, it is possible to bypass this restriction, as we'll see later.

Let's return to `say2.py`. When we called `say('hello')`, we passed the string `'hello'` as the argument. Thus, `'hello'` was assigned to the `text` parameter.

As mentioned earlier, one benefit that functions give us is the ability to make changes in one location. Suppose we want to add a `==>` to the beginning of every line that `say` outputs. All we have to do is change one line of code -- we don't have to change the function invocations:
    
    
    def say(text):
        # highlight
        print('==> ' + text)
        # endhighlight
    
    say('hello')        # ==> hello
    say('hi')           # ==> hi
    say('how are you')  # ==> how are you
    say("I'm fine")     # ==> I'm fine
    

Run this code to see the result. We've now added a `==>` to the beginning of each line. We only had to change a single line of code. Now, you're starting to see the power of functions.

## Return Values

As we've seen in some earlier examples, functions can perform an operation and return a result to the caller for later use. We do that with return values and the `return` statement.

All Python function calls evaluate to a value, provided the function doesn't raise an exception (an error). By default, that value is `None`; this is the **implicit return value** of most Python functions. However, when you use a `return` statement, you can return a specific value from a function. This is an **explicit return value**. There is no distinction between implicit and explicit return values outside the function. Still, it's important to remember that all functions return something unless they raise an exception, even if they don't explicitly execute a `return` statement.

Let's create an `add` function that returns the sum of two numbers:
    
    
    def add(a, b):
        return a + b
    
    add(2, 3)           # returns 5
    

When you run this program, it doesn't print anything since `add` doesn't call `print` or any other output functions. However, the function does return a value: `5`. When Python encounters the `return` statement, it evaluates the expression, terminates the function, then returns the expression's value to the location where we called `add`.

Let's capture the return value in a variable and print it to verify that:
    
    
    def add(a, b):
        return a + b
    
    # highlight
    two_and_three = add(2, 3)
    print(two_and_three)  # 5
    # endhighlight
    

Python uses the `return` statement to return a value to the code that invoked the function. If you don't specify a value, it returns `None`. Either way, the `return` statement terminates the function and returns control to the calling function.

Functions that always return a Boolean value, i.e., `True` or `False`, are called **predicates**. For example, the following function is a predicate:
    
    
    def is_digit(char):
        if char >= '0' and char <= '9':
            return True
    
        return False
    

You will almost certainly encounter this term in future readings and videos, so commit it to memory.

## Default Parameters

It's sometimes helpful to invoke a function without some of its arguments. You can do that by providing default values for the function's parameters. Let's update `say` to use a default value when the caller omits the argument.
    
    
    def say(text='hello'):
        print(text + '!')
    
    say('Howdy') # Howdy!
    say()        # hello!
    

Notice that invoking `say` without arguments, as on line 5, prints 'hello!'. We can invoke `say` without arguments since we've provided a default value for `text`. Nice!

You can provide defaults for any or all of a function's parameters. However, once you specify a default value for a parameter, all subsequent positional parameters must also have default values:
    
    
    def say(msg1, msg2, msg3='dummy message', msg4):
        pass
    # SyntaxError: non-default argument follows default argument
    

It's also worth noting that you can't accept the default value for a parameter and provide an explicit value for a subsequent parameter:
    
    
    def say(msg1, msg2, msg3='dummy message',
                        msg4='omitted message'):
        print(msg1)
        print(msg2)
        print(msg3)
        print(msg4)
    
    say('a', 'b', 'c', 'd')
    # a
    # b
    # c
    # d
    
    say('a', 'b', 'c')
    # a
    # b
    # c
    # omitted message
    
    say('a', 'b')
    # a
    # b
    # dummy message
    # omitted message
    
    say('a', 'b', , 'd')
    # a
    # b
    # d               # oops - expecting 'dummy message'
    # omitted message # oops again - expected 'd'
    

Python has a variety of ways to specify parameters. The easiest is with **positional parameters**. With positional parameters, the parameter values are taken from the corresponding argument position. Thus, if you have a function that takes 3 parameters, the first parameter is set to the first argument, the second parameter to the second argument, and the third parameter to the third argument. For instance, in the `say` function above, the 4 parameters are assigned based on the order of the arguments. Of course, default parameters mean you can omit some arguments.

We'll see some of Python's other parameter types later in the Core Curriculum.

## Functions vs. Methods

Thus far, all our function calls have used the `function_name(obj, ...)` syntax. We call a function by writing parentheses after its name. Any arguments the function needs are provided inside the parentheses.

However, suppose you want to convert a string to all uppercase letters. You might expect to use a function invocation like `upper(my_str)`. However, that won't work. You must use a different syntax called **method invocation**.

Method invocations occur when you prepend an object followed by a period (`.`) to a function invocation, e.g., `'xyzzy'.upper()`. We call such function invocations **method calls**. We also speak of the function as a **method**. We cover this topic in more detail in the Core Curriculum when we get to Object-Oriented Programming. You can think of the previous code as the function `upper` returning a modified version of the string `'xyzzy'`.

Methods provide the same benefits as functions. However, methods work with specific objects. All methods are functions but not vice versa. Every method belongs to a class and requires an object of that class to call it. For instance, in the following example, we're using the string object represented by `my_str` to call the `upper` method from the `str` class:
    
    
    my_str = 'abc-123-def'
    print(my_str.upper())         # ABC-123-DEF
    

Writing your own methods requires _classes_ , which is how you create custom data types in Python. We're not ready to write our own classes and methods at this point; you'll learn how to do that in our [Object Oriented Programming in Python book](/books/oo_python).

In Python, the distinction between functions and methods may sometimes seem fuzzy. Some function invocations look like method invocations. For instance, consider the `math` module from Python's standard libraries. The module provides some mathematical functions that any program can use. Once you import the module, you just call the functions you need:
    
    
    import math
    
    print(math.sqrt(5))           # 2.23606797749979
    

Wait. Is that a method call? It sure looks like one. It quacks like one. Since `math` references an object, `math.sqrt()` must be a method call. However, it is not. While `math` is technically a reference to a `module` object, we're not using it to perform operations on that object. The sole purpose of the `math` object here is to tell Python where to look for those functions.

For brevity, we often speak of functions when discussing functions and methods together. However, you should say _methods_ when discussing functions explicitly designed to require calling objects.

## Mutating the Caller

Sometimes, a method mutates the object used to invoke the method: it **mutates the caller**. In the following example, the `pop` method mutates the caller (the list referenced by `odd_numbers`):
    
    
    odd_numbers = [1, 3, 5, 7, 9]
    odd_numbers.pop()
    print(odd_numbers)  # [1, 3, 5, 7]
    

We can also talk about whether functions mutate their arguments. The following function illustrates this concept:
    
    
    def add_new_number(my_list):
        my_list.append(9)
    
    numbers = [1, 2, 3, 4, 5]
    add_new_number(numbers)
    print(numbers) # [1, 2, 3, 4, 5, 9]
    

This code uses the `list.append` method to add a new number to the list `my_list`.Thus, `list.append` mutates its caller. However, the `add_new_number` function doesn't mutate a caller (there is no caller). Instead, it mutates its argument.

In general, mutating the caller is acceptable practice; many built-in functions and methods do just that. However, you should avoid mutating arguments since such functions can be tough to debug and is considered poor practice. Almost no built-in functions mutate their arguments.
    
    
    # Returning a new object
    def add_new_number(my_list):
        return my_list + [9]
    
    numbers = [1, 2, 3, 4, 5]
    new_numbers = add_new_number(numbers)
    print(new_numbers) # [1, 2, 3, 4, 5, 9]
    print(numbers)     # [1, 2, 3, 4, 5]
    

How do you know which methods mutate the caller and which don't? That's easy when the caller is immutable: the answer is always, "This method does not mutate the caller." However, when the caller is mutable, there's no way to say without inspecting the method's code or checking the documentation.

We discuss object mutation in much more detail in our courses at Launch School.

## Summary

Functions and methods are fundamental concepts in Python programming. Knowing what a function does is crucial to your development as a Python programmer. You'll use them all the time in programs both big and small.

##  Exercises

  1. What happens when you run the following program? Why do we get that result?
    
        def set_foo():
        foo = 'bar'
    
    set_foo()
    print(foo)
    

#### Solution

The program outputs an error: `NameError: name 'foo' is not defined`

Since `foo` is created inside a function, it isn't in scope when executing code that isn't part of that function.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Take a look at this code snippet:
    
        foo = 'bar'
    
    def set_foo():
        foo = 'qux'
    
    set_foo()
    print(foo)
    

What does this program print? Why?

#### Solution

The program prints `bar` since the assignment on line 4 creates a new variable that is local to the function. That is, the `foo` variable on line 4 shadows the `foo` variable on line 1, so line 4 doesn't change the value of `foo` from line 1.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Write a program that uses a `multiply` function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.
    
        $ python multiply.py
    Enter the first number: 3.1416
    Enter the second number: 2.7183
    3.1416 * 2.7183 = 8.53981128
    

#### Solution
    
        def multiply(left, right):
        return left * right
    
    def get_number(prompt):
        entry = input(prompt)
        return float(entry)
    
    first_number = get_number('Enter the first number: ')
    second_number = get_number('Enter the second number: ')
    product = multiply(first_number, second_number)
    print(f'{first_number} * {second_number} = {product}')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Consider this code:
    
        def multiply_numbers(num1, num2, num3):
        result = num1 * num2 * num3
        return result
    
    product = multiply_numbers(2, 3, 4)
    

Identify the following items in that code:

Item  
---  
function name  
function arguments  
function definition  
function body  
function parameters  
function invocation  
function return value  
all identifiers  
  
#### Solution

Item | Answer  
---|---  
function name |  `multiply_numbers` on lines 1 and 5  
function arguments |  `2`, `3`, and `4` between the parentheses on line 5  
function definition | everything on lines 1-3  
function body | everything on lines 2 and 3  
function parameters |  `num1`, `num2`, and `num3` on line 1  
function invocation |  `multiply_numbers(2, 3, 4)` on line 5  
function return value | `24`  
all identifiers |  `multiply_numbers`, `num1`, `num2`, `num3`, `result`, and `product`  
  
**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

_Errata_ : At about 1:56 the instructor says that the function name is on lines 3 and 5. In fact, the correct line numbers in the video are lines 3 and 7.

  5. What does the following code print?
    
        def scream(words):
        return words + '!!!!'
    
    scream('Yipeee')
    

#### Solution

This program doesn't output anything. The function returns a value, `Yipeee!!!!`, but it doesn't do anything with it. In particular, it doesn't print it.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. What does the following code print?
    
        def scream(words):
        words = words + '!!!!'
        return
        print(words)
    
    scream('Yipeee')
    

#### Solution

This code also doesn't print anything. The `return` on line 3 terminates the function before it can print anything.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. Without running the following code, what do you think it will do?
    
        def foo(bar, qux):
        print(bar)
        print(qux)
    
    foo('Hello')
    

#### Solution

The code will raise an error:
    
        TypeError: foo() missing 1 required positional
    argument: 'qux'
    

We've defined `foo` with two parameters. However, we've only passed it one argument. This is an error.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. Without running the following code, what do you think it will do?
    
        def foo(bar, qux):
        print(bar)
        print(qux)
    
    foo(42, 3.141592, 2.718)
    

#### Solution

The code will raise an error:
    
        TypeError: foo() takes 2 positional arguments,
    but 3 were given
    

We've defined `foo` with two parameters. However, we've passed the function three arguments. This is an error.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  9. Without running the following code, what do you think it will do?
    
        def foo(first, second=3, third=2):
        print(first)
        print(second)
        print(third)
    
    foo(42, 3.141592, 2.718)
    

#### Solution

The code will print the following:
    
        42
    3.141592
    2.718
    

Here, we've defined `foo` with three parameters, with the `second` and `third` parameters having default values. However, we've passed all three arguments to the function, so Python ignores the default values.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  10. Without running the following code, what do you think it will do?
    
        def foo(first, second=3, third=2):
        print(first)
        print(second)
        print(third)
    
    foo(42, 3.141592)
    

#### Solution

The code will print the following:
    
        42
    3.141592
    2
    

Here, we've defined `foo` with three parameters, with the `second` and `third` parameters having default values. We've passed the function two arguments, so Python uses the default value for the last argument.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  11. Without running the following code, what do you think it will do?
    
        def foo(first, second=3, third=2):
        print(first)
        print(second)
        print(third)
    
    foo(42)
    

#### Solution

The code will print the following:
    
        42
    3
    2
    

Here, we've defined `foo` with three parameters, with the `second` and `third` parameters having a default value. We've passed the function one argument, so Python uses the default value for the last two parameters.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  12. Without running the following code, what do you think it will do?
    
        def foo(first, second=3, third=2):
        print(first)
        print(second)
        print(third)
    
    foo()
    

#### Solution

The code will raise an error:
    
        TypeError: foo() missing 1 required positional
    argument: 'first'
    

Here, we've defined `foo` with three parameters, with the `second` and `third` parameters having default values. We haven't passed the function any arguments. That's an error, though - the `first` parameter has no default value.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  13. Without running the following code, what do you think it will do?
    
        def foo(first, second=3, third):
        print(first)
        print(second)
        print(third)
    
    foo(42)
    

#### Solution

The code will raise an error:
    
        SyntaxError: non-default argument follows
    default argument
    

Here, we've defined `foo` with three parameters, with the `second` parameter having a default value. This is an error, however. Once Python sees a positional parameter with a default value, all subsequent parameters must have default values.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  14. Identify all of the identifiers on each line of the following code.
    
        def multiply(left, right):
        return left * right
    
    def get_num(prompt):
        return float(input(prompt))
    
    first_number = get_num('Enter the first number: ')
    second_number = get_num('Enter the second number: ')
    product = multiply(first_number, second_number)
    print(f'{first_number} * {second_number} = {product}')
    

#### Solution

The identifiers in this code are `multiply`, `left`, `right`, `first_number`, `second_number`, `get_num`, `prompt`, `float`, `input`, `product`, and `print`. The following table shows where each identifier appears in the code.

Identifier | Appears on these lines  
---|---  
`multiply` | 1, 9  
`left` | 1, 2  
`right` | 1, 2  
`first_number` | 7, 9, 10  
`second_number` | 8, 9, 10  
`get_num` | 4, 7, 8  
`prompt` | 4, 5  
`float` | 5  
`input` | 5  
`product` | 9, 10  
`print` | 10  
  
**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  15. Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.
    
        def multiply(left, right):
        return left * right
    
    def get_num(prompt):
        return float(input(prompt))
    
    first_number = get_num('Enter the first number: ')
    second_number = get_num('Enter the second number: ')
    product = multiply(first_number, second_number)
    print(f'{first_number} * {second_number} = {product}')
    

#### Solution

Category | Identifiers  
---|---  
Global |  `multiply`, `get_num`, `first_number`, `second_number`, `product`  
Local |  `left`, `right`, `prompt`  
Built-in |  `float`, `input`, `print`  
  
Functions defined in a program file are global identifiers unless those functions are defined as an object property or nested inside another function. Thus, `multiply`, `get_num`, and `product` are globals in this program. Function parameters and variables initialized inside a function are always local identifiers. Thus, `left`, `right`, and `prompt` are all local variables. `first_number` and `second_number` are initialized as global variables on lines 7 and 8 respectively, then used on lines 9 and 10.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  16. In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.
    
        def multiply(left, right):
        return left * right
    
    def get_num(prompt):
        return float(input(prompt))
    
    first_number = get_num('Enter the first number: ')
    second_number = get_num('Enter the second number: ')
    product = multiply(first_number, second_number)
    print(f'{first_number} * {second_number} = {product}')
    

#### Solution

     * Function names: 
       * `multiply`: defined on line 1, used on line 9. 
       * `get_num`: defined on line 4, used on lines 7 and 8. 
       * `float`: built-in function used on line 5. 
       * `input`: built-in function used on line 5. 
       * `print`: built-in function used on line 10. 
     * Parameters: 
       * `left` and `right` are defined on line 1 and then used on line 2. 
       * `prompt` is defined on line 4 and then used on line 5. 

Note that `left` and `right` are defined as parameters for the `multiply` function on line 1. We reference those parameters on line 2, but usually speak of them as local variables instead of parameters. For this exercise, it's okay if you said that `left` and `right` are present on line 2. It's also okay if you omitted it.

Likewise, `prompt` is defined as a parameter for the `get_num` function on line 4, but used as a local variable on line 5.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  17. Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?
    
        def say(message):
        print(f'==> {message}')
    
    string1 = input()
    string2 = input()
    
    say(max(string1.upper(), string2.lower()))
    

#### Solution

Function Names | Method Names | Built-in Function Names  
---|---|---  
`say` |  |   
|  | `print`  
|  | `input`  
|  | `max`  
| `upper` |   
| `lower` |   
  
If you identified all the method and built-in function names as function names, that's an acceptable answer as well: all methods are functions, and built-in functions are just functions that are, well, built-in.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  18. The following function returns a list of the remainders of dividing the numbers in `numbers` by 3:
    
        def remainders_3(numbers):
        return [number % 3 for number in numbers]
    

Use this function to determine which of the following lists contains at least one number that is **not** evenly divisible by 3 (that is, the remainder is not `0`):
    
        numbers_1 = [0, 1, 2, 3, 4, 5, 6]
    numbers_2 = [1, 2, 4, 5]
    numbers_3 = [0, 3, 6]
    numbers_4 = []
    

Note: when working with integers, a value of `0` is "falsy"; all other integers are "truthy".

#### Solution
    
        print(any(remainders_3(numbers_1)))     # True
    print(any(remainders_3(numbers_2)))     # True
    print(any(remainders_3(numbers_3)))     # False
    print(any(remainders_3(numbers_4)))     # False
    

`remainders_3` returns a list of integers between 0 and 2, inclusive. A value of `0` means the corresponding number is divisible by 3, while a value of `1` or `2` means the number is **not** divisible by 3. Since `0` is falsy and `1` and `2` are truthy, we can use `any` to determine whether any of the numbers are non-zero.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  19. The following function returns a list of the remainders of dividing the numbers in `numbers` by 5:
    
        def remainders_5(numbers):
        return [number % 5 for number in numbers]
    

Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:
    
        numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
    numbers_3 = [0, 5, 10]
    numbers_4 = []
    

Note: when working with integers, a value of `0` is "falsy"; all other integers are "truthy".

#### Solution
    
        print(all(remainders_5(numbers_1)))     # False
    print(all(remainders_5(numbers_2)))     # True
    print(all(remainders_5(numbers_3)))     # False
    print(all(remainders_5(numbers_4)))     # True
    

`remainders_5` is similar to `remainders_3` in the previous exercise in that it returns a list of integers. In this list, a value of `0` means the corresponding number is divisible by 5, while a non-zero value means the number is **not** divisible by 5. Since `0` is falsy and the other integers are truthy, we can use `all` to determine whether all of the numbers are not divisible by `5`.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Flow Control

A computer program is like a journey for your data. Data encounters situations that impact it during this journey, changing it forever. Like any journey, one has a choice of routes to reach the destination. Sometimes, data takes one path; sometimes, another. Which roads the data takes depends on the program's end goal.

When writing programs, you want your data to take the correct path. You want it to turn left or right, up, down, reverse, or proceed straight ahead when it's supposed to. We call this **flow control**.

How do we make data do the right thing? We use conditionals.

## Conditionals

A conditional is a fork, or multiple forks, in the road. When your data arrives at a conditional, Python evaluates the conditional and tells the data where to go. The simplest conditionals use a combination of `if` statements with comparison and logical operators (`<`, `>`, `<=`, `>=`, `==`, `!=`, `and`, `or`, and `not`) to direct traffic. They use the keywords `if`, `elif`, and `else`.

That's enough talking; let's write some code. Create a file named `conditional.py` with the following content:
    
    
    value = int(input('Enter a number: '))
    
    if value == 3:
        print('value is 3')
    

Run `conditional.py` at least twice.

  * The first time, enter the value `3`. 
  * The second and subsequent times, input any other integer value. 



This example shows the simplest of `if` statements: it has a single **block** (one or more Python statements or expressions) that executes when the condition (`value == 3`) is `True`. Otherwise, Python bypasses the block. Regardless, execution eventually resumes with the first statement or expression after the `if` statement.

Thus, if the input value is `3`, this code prints `value is 3`. The code doesn't print anything if the user inputs any other integer.

We can expand the `if` statement to include some code that runs when `value` is not `3`:
    
    
    value = int(input('Enter a number: '))
    
    if value == 3:
        print('value is 3')
    # highlight
    else:
        print('value is NOT 3')
    # endhighlight
    

Here, Python prints `value is 3` if the user enters `3`; otherwise, it prints `value is NOT 3`.

Note that the `else` block isn't a proper statement; it's part of the `if` statement.

We can nest `if` statements inside an outer `if`. In this next example, we nest an `if` statement inside the `else` block of the outer `if`:
    
    
    value = int(input('Enter a number: '))
    
    if value == 3:
        print('value is 3')
    else:
        # highlight
        if value == 4:
            print('value is 4')
        else:
            print('value is NOT 3 or 4')
        # endhighlight
    

This time, run `conditional.py` at least three times:

  * The first time, enter the value 3. 
  * The second time, enter the value 4. 
  * The third and subsequent times, input any other integer value. 



The indentation levels show how the code is supposed to work. In this case, Python:

  * prints `value is 3` if the user inputs `3`. 
  * prints `value is 4` if the user inputs `4`. 
  * prints `value is NOT 3 or 4` if the user enters any other integer. 



The sequence of operations begins on line 3, where we compare the user input against `3`. If yes, line 4 runs; otherwise, we drop down to the `else` block. In the `else` block, we compare the input against `4` on line 6. If yes, line 7 runs; otherwise, we drop down to the inner `else` block and run the code on line 9.

We recommend avoiding nested `if` statements when possible. They quickly become difficult to read with multiple levels of nesting or longish code blocks. However, don't get twisted up trying to avoid them entirely. Keep the nesting to a modest 2 or 3 levels deep and use functions to isolate some of the more complex code.

You can rewrite the previous example using an `elif` block:
    
    
    if value == 3:
        print('value is 3')
    elif value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')
    

The `elif` block runs if `value == 3` is `False` and `value == 4` is `True`. The code produces the same results as the nested `if`.

You can have as many `elif` blocks as you need, but they all need to be after the `if` block and, if the code has one, before the `else` block. The `elif` conditionals are evaluated in the order they appear in the code.

Finally, `if` statement blocks may contain as many lines as you need:
    
    
    if value == 3:
        print('value is 3')
        print('value is an odd number')
        print('value is a prime number')
    elif value == 4:
        print('value is 4')
        print('value is an even number')
        print('value is NOT a prime number')
    elif value == 9:
        print('value is 9')
        print('value is an odd number')
        print('value is NOT a prime number')
    else:
        print('value is something else')
    

Every once in a while, you may want to create a block in an `if` statement that does nothing. We usually do this for readability purposes. However, blocks can't be empty. Instead, you have to use a `pass` statement.
    
    
    if value == 3:
        print('value is 3')
    elif value == 4:
        print('value is 4')
    elif value == 9:
        pass # We don't care about 9
    else:
        print('value is something else')
    

Adding a comment to a `pass` is good practice so future programmers know why it is there.

All statements in a block must be indented from the statement that begins the block. The indentation in a block must be consistent. If the first line of the block is indented 4 spaces, all statements in the block must be indented 4 spaces.

Nested blocks should be indented more than the containing block. For instance, if the current block is indented by 4 spaces from the outer block (the conventional amount of indentation), then a nested block inside that block should be indented by 8 spaces. Another nested block would bring the indentation to 12 spaces.

Be careful with your indentation. If you accidentally outdent some code, that will end the block. For instance:
    
    
    if value == 1:
        print('value is one')
    print('the value is odd')
    

If you meant to print both messages when `value` is `1`, that's what will happen. However, Python will display the second message even if `value` is not 1.

## Comparisons

Let's look at the comparison operators in some more depth so you can build more complicated conditional statements. Remember that comparison operators return a Boolean value: `True` or `False`.

The expressions to the left and right of an operator are its **operands**. For instance, the equality comparison `x == y` uses the `==` operator with two operands, `x` and `y`.

  * **`==`**

The **equality operator** returns `True` when the operands have equal values, `False` otherwise. We discussed `==` briefly in the [Basics Operations chapter](/books/python/read/basic_ops). It should be familiar, even if it still looks strange.
    
        print(5 == 5)                 # True
    print(5 == 4)                 # False
    
    print('abc' == 'abc')         # True
    print('abc' == 'abcd')        # False
    
    print(5 == '5')               # False
    
    print([1, 2, 3] == [1, 2, 3]) # True
    print([1, 2, 3] == [3, 2, 1]) # False
    

In most cases, operands must have the same type and value to be equal. Thus, `5` is not equal to `'5'`. There are some places where you can mix types, however. For instance, integers and floats that are mathematically equivalent are usually, but not always, considered equal:
    
        print(5 == float(5))                # True
    
    big_num = 12345678901234567
    print(float(big_num) == big_num)    # False
    

Enormous floats lack precision at around 18 significant digits on most modern machines. That can lead to surprises if you happen to work with big numbers.

Comparisons with strings are case-sensitive. Thus, `'abc'` is not equal to `'aBc'`. You can use the `str.lower` and `str.upper` methods to achieve a case-insensitive comparison:
    
        print('abc' == 'aBc')                 # False
    print('abc'.lower() == 'aBc'.lower()) # True
    print('abc'.upper() == 'aBc'.upper()) # True
    

In some non-US alphabets, converting text to upper or lower case isn't straightforward. For instance, in German, `'straße'` and `strasse` are considered equivalent. However, the following code prints `False`:
    
        'straße'.lower() == 'strasse'.lower()
    

The `str.casefold` method makes allowances for this issue and does the right thing:
    
        'straße'.casefold() == 'strasse'.casefold()
    

While `casefold` is only needed when working with non-US characters, it's best practice in Python to use `casefold` instead of `lower` or `upper`, especially when comparing strings.

  * **`!=`**

The **inequality operator** , `!=`, is `==`'s inverse: It returns `False` when `==` would return `True`, and `True` when `==` would return `False`. It returns `False` when the operands have the same type and value, `True` otherwise. Other than the return value, the behaviors of `==` and `!=` are identical.
    
        print(5 != 5)             # False
    print(5 != 4)             # True
    print('abc' != 'abc')     # False
    print('abc' != 'aBc')     # True
    print(5 != '5')           # True
    

  * **`<` and `<=`**

The **less than operator** (`<`) returns `True` when the value of the left operand has a value that is less than the value on the right, `False` otherwise. The **less than or equal to operator** (`<=`) is similar, but it also returns `True` when the values are equal; `<` returns `False` when the operands are equal.
    
        print(4 < 5)              # True
    print(5 < 4)              # False
    print(5 < 5)              # False
    
    print(4 <= 5)             # True
    print(5 <= 4)             # False
    print(5 <= 5)             # True
    
    print('4' < '5')          # True
    print('5' < '4')          # False
    print('5' < '5')          # False
    
    print('42' < '402')       # False
    print('42' < '420')       # True
    print('420' < '42')       # False
    

The examples with strings are especially tricky here! Make sure you understand them. Python compares strings character-by-character, moving from left to right. It looks for the first character that differs from its counterpart in the other string. Once it finds differing characters, it compares them to determine the relationship.

If both strings are equal up to the shorter string's length, as in the last two examples, the shorter one is considered less than the longer one.

  * **`>` and `>=`**

The **greater than operator** (`>`) returns `True` when the value of the left operand has a value that is greater than the value on the right, `False` otherwise. The **greater than or equal to operator** (`>=`) is similar, but it also returns `True` when the values are equal; `>` returns `False` when the operands are equal.
    
        print(4 > 5)              # False
    print(5 > 4)              # True
    print(5 > 5)              # False
    
    print(4 >= 5)             # False
    print(5 >= 4)             # True
    print(5 >= 5)             # True
    
    print('4' > '5')          # False
    print('5' > '4')          # True
    print('5' > '5')          # False
    
    print('42' > '402')       # True
    print('42' > '420')       # False
    print('420' > '42')       # True
    

As with `<` and `<=`, you can compare strings with the `>` and `>=` operators; the rules are similar.




## Logical Operators

You're beginning to get a decent grasp of basic conditional flow. Let's take a few minutes to see how we can combine conditions to create more complex scenarios. The `not`, `and`, and `or` **logical operators** provide the ability to combine conditions:

  * **`not`**

The **not operator** returns `True` when its operand is `False` and returns `False` when the operand is `True`. That is, it negates its operand.
    
        print(not True)           # False
    print(not False)          # True
    print(not(4 == 4))        # False
    print(not(4 != 4))        # True
    

In these examples, Python first evaluates the expression on the right, then applies `not` to the result, thus negating it. For instance, we know that `4 == 4` is `True`, so `not(4 == 4)` is `False`.

You can omit the parentheses in the last two examples. However, we don't recommend it. Operator precedence issues may occur if you let Python decide which operator to evaluate first. Use parentheses if you have anything more complex than a single identifier or literal to the right of `not`.

Unlike most operators, `not` takes a single operand; it appears to the operator's right. Operators that take only one operand are called **unary operators**. Operators that take two operands are **binary operators** , though you'll rarely hear that term.

  * **`and` and `or`**

The **and operator** returns `True` when both operands are `True`. It returns `False` when either operand is `False`. The **or operator** returns `True` when either operand is `True` and `False` when both operands are `False`.

The following **truth** table shows how `True` and `False` interact with the `and` and `or` operators. You should memorize this table:

A | B | A and B | A or B  
---|---|---|---  
`True` | `True` | `True` | `True`  
`True` | `False` | `False` | `True`  
`False` | `True` | `False` | `True`  
`False` | `False` | `False` | `False`  
  
For completeness, let's see a few examples:
    
        print((4 == 4) and (7 == 7))        # True
    print((4 == 4) and (7 == 3))        # False
    print((4 == 9) and (7 == 7))        # False
    print((4 == 9) and (7 == 3))        # False
    
    
        print((4 == 4) or (7 == 7))         # True
    print((4 == 4) or (7 == 3))         # True
    print((4 == 9) or (7 == 7))         # True
    print((4 == 9) or (7 == 3))         # False
    

As with `not`, parentheses aren't always needed. However, the same "precedence" issues may occur. Always use parentheses if the corresponding operand is not a literal or identifier.




## Short Circuits

The `and` and `or` operators use a mechanism called **short circuit evaluation** to evaluate their operands. Consider these two expressions:
    
    
    is_red(item) and is_portable(item)
    is_green(item) or has_wheels(item)
    

The first expression returns `True` when `item` is red and portable. If either condition is `False`, then the overall result **must** be `False`. Thus, if the program determines that `item` is not red, it doesn't have to determine whether it is also portable. Python short-circuits the rest of the expression by terminating evaluation if it determines that `item` isn't red. It doesn't need to call `is_portable()` since it already knows the expression must be `False`.

Similarly, the second expression returns `True` when `item` is either green or has wheels. When either condition is `True`, the overall result **must** be `True`. Thus, if the program determines that `item` is green, it doesn't have to decide whether it has wheels. Again, Python short-circuits the entire expression once it knows that `item` is green; the expression must be `True`.

## Truthiness

Many languages can evaluate objects and values as either **truthy** or **falsy**. Python is no slouch here; it can too. It can evaluate every object's **truthiness**. Note that these terms are _not synonymous_ with `True`, `False`, and Boolean. In addition, truthy and falsy are not actual objects or values. Instead, they are terms that describe how specific objects behave in a Boolean context.

Truthiness arises in conditional expressions, such as `if` and `while` statements. Conditional expressions don't need to produce Boolean values. Instead, Python only needs to determine their truthiness. In an `if` statement, a conditional expression that evaluates as truthy causes the `if` block to execute. The `else` or `elif` block runs when the expression evaluates as falsy.

Since conditionals only care about truthiness, we can use any expression as the condition. The expression will always be evaluated as truthy or falsy.

So, which values are truthy? Which are falsy? The built-in falsy values are as follows:

  * `False`, `None`
  * all numeric `0` values (integers, floats, complex) 
  * empty strings: `''`
  * empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`
  * Custom data types can also define additional falsy value(s). 



Okay, now that we know what's falsy, what's truthy? _Everything_ else.

Enough yammering. Let's see some examples:
    
    
    value = 5                     # 5 is truthy
    if value:
        print(f'{value} is truthy')
    else:
        print(f'{value} is falsy')
    
    
    
    value = 0                     # 0 is falsy
    if value:
        print(f'{value} is truthy')
    else:
        print(f'{value} is falsy')
    

The first example prints `5 is truthy` while the second prints `0 is falsy`. This works since Python evaluates `5` as truthy and `0` as falsy.

You may sometimes see articles that speak of _true_ and _false_ values; this even happens in the Python documentation. The authors should probably talk of truthy and falsy evaluations, instead, not true and false. At Launch School, we want you to use truthy and falsy when speaking of truthiness, `True` and `False` when talking of booleans, and true and false when discussing truths and falsehoods.

You may have noticed how we took care to say things like _evaluates as truthy_. For brevity, you can simply describe expressions as either truthy or falsy. The "evaluates as" terminology is unnecessary.

### Truthiness and Short-Circuit Evaluation

You may recall that the `and` and `or` logical operators cause short-circuit evaluation. You may not realize that the logical operators don't always return `True` or `False`. Both operators care only about the truthiness of their operands. The final value returned by an expression using `and` and `or` is the value of the final sub-expression evaluated by Python:
    
    
    print(3 and 'foo')   # last evaluated op: 'foo'
    print('foo' and 3)   # last evaluated op: 3
    print(0 and 'foo')   # last evaluated op: 0
    print('foo' and 0)   # last evaluated op: 0
    
    
    
    print(3 or 'foo')    # last evaluated op: 3
    print('foo' or 3)    # last evaluated op: 'foo'
    print(0 or 'foo')    # last evaluated op: 'foo'
    print('foo' or 0)    # last evaluated op: 'foo'
    print('' or 0)       # last evaluated op: 0
    print(None or [])    # last evaluated op: []
    

Suppose you have a logical expression that returns a non-Boolean object instead of a Boolean:
    
    
    foo = None
    bar = 'qux'
    is_ok = foo or bar
    

In this code, `is_ok` gets set to the truthy value, `'qux'`. In most cases, you can use `'qux'` as though it were a Boolean `True` value. However, using a string as a Boolean isn't always the best way to write your code. It may even look like a mistake to another programmer trying to track down a bug. In some strange cases, it may even be a mistake.

You can readily address this with an `if`/`else` statement:
    
    
    if foo or bar:
        is_ok = True
    else:
        is_ok = False
    

This snippet sets `is_ok` to either `True` or `False` based on the truthiness of `foo or bar`. However, it is wordy. Many Python programmers would write this more concisely as:
    
    
    is_ok = bool(foo or bar)
    

## Logical Operator Precedence

As discussed in an earlier chapter, Python has **precedence** rules for evaluating expressions that use multiple operators and sub-expressions. The following list shows the precedence of the comparison operators from highest (top) to lowest (bottom).

  * `==`, `!=`, `<=`, `<`, `>`, `>=` \- Comparison 
  * `not` \- Logical NOT 
  * `and` \- Logical AND 
  * `or` \- Logical OR 



Thus, if you have an expression like `not x == y`, you can know that `x == y` is evaluated first, then `not` is applied to the overall result. That is, `not x == y` is equivalent to `not(x == y)`.

Things get really confusing when combining `and` and `or` in an expression. Even though `and` has higher precedence than `or`, the fact that both are short-circuiting operators adds a whole lot of complexity. For example, can you determine what the following code prints?
    
    
    print(1 or 2 and 3)
    print(0 or 2 and 3)
    print(1 or 0 and 3)
    print(1 or 2 and 0)
    print(0 or 0 and 3)
    print(0 or 2 and 0)
    print(1 or 0 and 0)
    print(0 or 0 and 0)
    
    print(1 and 2 or 3)
    print(0 and 2 or 3)
    print(1 and 0 or 3)
    print(1 and 2 or 0)
    print(0 and 0 or 3)
    print(0 and 2 or 0)
    print(1 and 0 or 0)
    print(0 and 0 or 0)
    

Go ahead and guess what will be output, then try running the code to see the results. In all likelihood, you will guess incorrectly at least once.

We're not going to try to explain what's happening with this code. While you might encounter some code like this in the future, the mixed `and`/`or` code will likely only be a small part of your problems.

In short: **do not write code like this**! If you must mix `and` and `or`, use parentheses to control how the code gets written. For instance, compare these two lines of code:
    
    
    print((a and b) or (c and d))
    print(a and b or c and d)
    

The first line, while complex, is easier to understand than the second.

To repeat, avoid mixing `and` and `or` in a single expression unless you use parentheses to control the order of evaluation.

## match/case Statement

The last conditional flow structure we want to discuss is the `match`/`case` statement (or, more concisely, the `match` statement). A `match` statement, in it's most basic form, is similar to an `if` statement but has a different interface. It compares a single value against multiple values, whereas `if` can test multiple expressions with any condition.

The Python `match` statement was introduced in Python 3.10. You won't be able to use it in earlier versions, such as the 3.9 version provided by Cloud9 with the Amazon Linux 2023 operating system. However, it's straightforward to rewrite the `match` statements we will use as `if` statements.

`match` statements use the reserved words `match` and `case`. It's often easier to show rather than tell, and that's certainly the case with the `match` statement. First, create a file named `match.py` with this content:
    
    
    value = 5
    
    match value:
        case 5:
            print('value is 5')
        case 6:
            print('value is 6')
        case _: # default case
            print('value is neither 5 nor 6')
    # value is 5
    

This example is functionally identical to the following `if/else` statement:
    
    
    value = 5
    
    if value == 5:
        print('value is 5')
    elif value == 6:
        print('value is 6')
    else:
        print('value is neither 5 nor 6')
    # value is 5
    

You can see how similar they are, but you can also see how they differ. The `match` statement evaluates the expression `value`, compares its value to the value in each `case`, and executes the block associated with the first matching `case`. In this example, the value of the expression is `5`; thus, the program executes the statements associated with `case 5`. The statements in the `case _` block run when the expression doesn't match any other `case` blocks. It acts like the final `else` in an `if` statement and must be the last `case` block in the `match` statement.

If you want to match multiple values in a case, you can do so by using the `|` character to separate item values:
    
    
    value = 5
    
    match value:
        case 1 | 2 | 3 | 4:
            print('value is < 5')
        case 5 | 6:
            print('value is 5 or 6')
        case _: # default case
            print('value is not 1, 2, 3, 4, 5, or 6')
    # value is 5 or 6
    

There are plenty of uses for `match` statements. They also have "pattern matching" abilities (which are beyond the scope of this book). They're potent tools in Python. If you're uncomfortable with them, play with the ones we presented above and watch how they respond to your changes. Test their boundaries and learn their capabilities. Curiosity will serve you well in your journey towards mastering Python. There is much to discover!

## Ternary Expressions

We wanted to briefly show you something we call **ternary expressions**. The official name is _conditional expression_ , but that's confusing since something like `a == b` is also a conditional expression. It is also sometimes called a _ternary operator_. However, it's not an operator.

A ternary expression is a concise way to choose between two values based on some condition. They are often used as an expression on the right side of an assignment, as function arguments, and as function return values.

Ternary expressions have the following structure:
    
    
    value1 if condition else value2
    

Python first evaluates the `condition`. If it's truthy, the expression returns `value1`. Otherwise, it returns `value2`. Note that only one of `value1` and `value2` will be evaluated.

Consider the following code:
    
    
    if shape.sides() == 3:
        print("Triangle")
    else:
        print("Square")
    

That's easy enough to understand, but it is a bit wordy. We can eliminate the wordiness at the sacrifice of a little clarity:
    
    
    print("Triangle" if shape.sides() == 3 else "Square")
    

Ternaries work particularly well when you need a way to handle missing or invalid data in output:
    
    
    print('N/A' if value == None else value)
    

Should you use ternary expressions in your code? We recommend using them only when it doesn't sacrifice too much clarity. Don't use them as a substitute for every 4-line `if`/`else` statement or as a way to save keystrokes: they work best as expressions.

Remember that many Python programmers dislike ternary expressions since they are hard to read. If you decide that you like ternary expressions, that's fine. However, use them judiciously. In particular, ternaries should almost always be extremely simple and fit entirely on one 79-column line of code.

## Summary

This chapter covered conditionals, comparisons, logical operators, and truthiness to control the flow of code execution. These are fundamental tools you'll need to become a Python developer.

##  Exercises

  1. To what values do the following expressions evaluate?
    
        False or (True and False)
    True or (1 + 2)
    (1 + 2) or True
    True and (1 + 2)
    False and (1 + 2)
    (1 + 2) and True
    (32 * 4) >= 129
    False != (not True)
    True == 4
    False == (847 == '847')
    

#### Solution
    
        False or (True and False)     # False
    True or (1 + 2)               # True
    (1 + 2) or True               # 3
    True and (1 + 2)              # 3
    False and (1 + 2)             # False
    (1 + 2) and True              # True
    (32 * 4) >= 129               # False
    False != (not True)           # False
    True == 4                     # False
    False == (847 == '847')       # True
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Write a function, `even_or_odd`, that determines whether its argument is an even or odd number. If it's even, the function should print `'even'`; otherwise, it should print `'odd'`. Assume the argument is always an integer.

Hint 1

A number is even if you can divide it by two with no remainder. For instance, `4` is even since `4` divided by `2` has no remainder. Conversely, `3` is odd since `3` divided by `2` has a remainder of `1`.

Hint 2

To determine the remainder, you can use the `%` modulo operator shown in _The Basics_ chapter.

#### Solution
    
        def even_or_odd(number):
        if number % 2 == 0:
            print('even')
        else:
            print('odd')
    
    
        def even_or_odd(number):
        print('even' if number % 2 == 0 else 'odd')
    

The solutions use the [modulo operator (%)](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) to determine whether the number is even. If the result of `number % 2` is `0`, the number is even.

The second solution shows the equivalent solution using a ternary expression. The author isn't sure whether this is more readable than the first solution.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Without running the following code, what does it print? Why?
    
        def bar_code_scanner(serial):
        match serial:
            case '123':
                print('Product1')
            case '113':
                print('Product2')
            case '142':
                print('Product3')
            case _:
                print('Product not found!')
    
    bar_code_scanner('113')
    bar_code_scanner(142)
    

#### Solution

The output is:
    
        Product2
    Product not found!
    

The first call to `bar_code_scanner` prints `Product2` since the first `case` that matches `'113'` is the one on line 5. The second call prints `Product not found!` since the numeric value 142 doesn't match any of the `case` statements with string arguments. Instead, it matches the `_` "default" `case`.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Refactor this statement to use a regular `if` statement instead.
    
        return ('bar' if foo() else qux())
    

#### Solution
    
        if foo():
        return 'bar'
    else:
        return qux()
    

Ternaries are most useful when both result values are given by simple expressions; anything more complicated than calling a function or accessing a variable or literal value can lead to unreadable code. Our original code is an excellent example of using the ternary expression; the refactoring merely demonstrates how the ternary works.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. What does this code output, and why?
    
        def is_list_empty(my_list):
        if my_list:
            print('Not Empty')
        else:
            print('Empty')
    
    is_list_empty([])
    

#### Solution

The output is `Empty` since an empty list like `[]` is falsy. As a result, `my_list` on line 2 is falsy, so the `else` block runs instead of the `if` block.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change `'hello world'` to `'HELLO WORLD'`, but don't change `'goodbye'`.

#### Solution
    
        def caps_long(string):
        if len(string) > 10:
            return string.upper()
        else:
            return string
    
    print(caps_long("Sue Smith"))     # Sue Smith
    print(caps_long("Sue Roberts"))   # SUE ROBERTS
    print(caps_long("Joe Shea"))      # Joe Shea
    print(caps_long("Joe Stevens"))   # JOE STEVENS
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. Write a function that takes a single integer argument and prints a message that describes whether:

     * the value is between 0 and 50 (inclusive) 
     * the value is between 51 and 100 (inclusive) 
     * the value is greater than 100 
     * the value is less than 0 
    
        number_range(0)     # 0 is between 0 and 50
    number_range(25)    # 25 is between 0 and 50
    number_range(50)    # 50 is between 0 and 50
    number_range(75)    # 75 is between 51 and 100
    number_range(100)   # 100 is between 51 and 100
    number_range(101)   # 101 is greater than 100
    number_range(-1)    # -1 is less than 0
    

#### Solution
    
        def number_range(number):
        if number < 0:
            print(f'{number} is less than 0')
        elif number <= 50:
            print(f'{number} is between 0 and 50')
        elif number <= 100:
            print(f'{number} is between 51 and 100')
        else:
            print(f'{number} is greater than 100')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Introduction to Collections

## Collection Types

Python has a surprisingly large number of built-in and auxiliary **collection** types. Collections are objects that contain zero or more member objects, often called **elements**. There are 3 main categories of collection: sequences, mappings, and sets.

Let's recap the types table from the [Data Types](/books/python/read/data_types#datatypes) chapter. We've reproduced a portion of the table below:

Type | Class | Category | Kind | Mutable  
---|---|---|---|---  
ranges | `range` | sequences | Non-primitive | No  
tuples | `tuple` | sequences | Non-primitive | No  
lists | `list` | sequences | Non-primitive | **Yes**  
dictionaries | `dict` | mappings | Non-primitive | **Yes**  
sets | `set` | sets | Non-primitive | **Yes**  
frozen sets | `frozenset` | sets | Non-primitive | No  
  
As you can see, the collections fall into several categories: sequences, mappings, and sets.

We often also include text sequences when talking about collections:

Type | Class | Category | Kind | Mutable  
---|---|---|---|---  
strings | `str` | text sequences | Primitive | No  
  
The primary text sequence of interest is strings. **Strings and other text sequences are not collections** , however. They are sufficiently similar that we can treat them as sequence collections, but its important to remember that they are not. For the purposes of this chapter, we will discuss text sequences as though they were collections.

Some collections are mutable; others are immutable. Keeping them straight takes some practice; be patient. In particular, lists and tuples differ only in that lists are mutable; tuples are not. The set collections differ similarly: sets are mutable; frozen sets are not.

We've met all these types earlier in this book. In this lesson, we'll explore them in depth.

## What are Sequences?

**Sequences** are types that maintain an **ordered** collection of objects (also: elements or values) that can be **indexed** by whole numbers. Ordered collections are collections organized in some sequence: a first element, a second element, a third element, and so on. Indexed sequences associate every object member with a whole number (0, 1, 2, etc.) that can be used to access or modify that object. The built-in sequences (ranges, lists, and tuples) always have the first object at index 0, the second at index 1, and so on.
    
    
    letters = ['a', 'b', 'c']
    print(letters[0])         # a (first element)
    print(letters[1])         # b (second element)
    print(letters[2])         # c (third element)
    

Lists and tuples are **heterogeneous** ; they may contain different kinds of objects, including other sequences:
    
    
    my_list = [
        'May',
        2.99,
        {None, True, False},
        [1, 2, 3],
    ]
    

Ranges are **homogenous** ; they always contain integers.

Strings are a form of sequence called a **text sequence**. They differ from ordinary sequences in several ways:

  1. Strings are homogenous; all characters in a string are, um, characters. 
  2. Characters are not a distinct kind of object; they are merely strings of length 1. 
  3. A string's individual characters are not separate strings until you reference a character. 
  4. Strings are not actual collections since the characters inside the string aren't objects. 



Bullet 3 merits an example, but it requires using Unicode. The Greek letter theta (**θ**) is a fine choice. Let's look at two snippets, one using a list and the other a string:
    
    
    letters = ['a', 'b', 'θ', 'd', 'e']
    char = letters[2]
    print(char is letters[2])     # True
    
    
    
    letters = 'abθde'
    char = letters[2]
    print(char is letters[2])     # False
    

Example 1 shows that `letters[2]` returns the object at index 2 of the `letters` list. Both `char` and `letters[2]` reference the same object, as shown on line 3.

However, in Example 2, the two characters are not the same object. They have the same value but are distinct objects.

We used `θ` to avoid [interning](/books/python/read/functions_methods#interning), a topic we discussed earlier. Python would have interned any character from the extended ASCII character set, and both snippets would have returned `True`. By switching to a non-ASCII character, we could show that characters in a string aren't objects.

While there are differences, we can usually treat strings as ordinary sequences.

## What are Sets?

**Sets** are types that maintain an **unordered** collection of unique objects (also called elements or **members**). Unlike sequences, sets cannot be indexed. Unordered means no well-defined order exists for the objects in a set. In fact, the sets `{1, 2, 3}` and `{3, 1, 2}` are equal since the order doesn't matter. By unique, we mean a set can not have duplicate members.

Python has two main built-in set types: sets and frozen sets. Regular sets are mutable; frozen sets are immutable. This is the only significant difference between the two:
    
    
    letters = {'a', 'b', 'c'}
    letters.add('d')
    print(letters)
    # {'a', 'b', 'c', 'd'} (order may differ)
    
    frozen_letters = frozenset(letters)
    frozen_letters.add('e')
    # AttributeError: 'frozenset' object has no
    # attribute 'add'
    

Sets and frozen sets, like Lists and tuples, are **heterogeneous** ; they may contain different kinds of objects, including other hashable collections:
    
    
    my_set = {
        'May',
        2.99,
        (None, True, False),
        range(5),
    }
    

Python will ignore any attempt to add duplicate members to a set:
    
    
    letters = {'a', 'b', 'c', 'b', 'a'}
    print(letters)
    # {'a', 'c', 'b'} (order may differ)
    
    letters.add('c')
    print(letters)
    # {'a', 'c', 'b'} (order may differ)
    

Since Python 3.7, sets of integers sometimes seem to be ordered. For instance:
    
    
    numbers = { 1, 2, 3, 4, 5 }
    print(numbers)      # { 1, 2, 3, 4, 5 }
    
    numbers = { 5, 3, 1, 2, 4 }
    print(numbers)      # { 1, 2, 3, 4, 5 }
    

No matter how often you run that code, it prints both sets with the same ordered values. It's an illusion, however, produced by an implementation detail. The behavior isn't guaranteed: it's easy to construct sets of integers that are clearly unordered:
    
    
    numbers = { 1, 2, 37, 4, 5 }
    print(numbers)      # {1, 2, 4, 37, 5}
    

The order of the numbers you see may not match ours, but you will likely see that the numbers are no longer predictably ordered.

## What are Mappings?

**Mappings** are types that maintain an **unordered** collection of key/value pairs (also called elements or members). Unlike sequences, mappings are accessed by their keys, which usually are not numbers. While Python has several mapping types, the only one we'll meet in this book is the **dictionary** or **dict** type.

Dicts have the following characteristics:

  * Dicts are mutable. 
  * The keys in a dict must be unique. Trying to add a duplicate key to a dict merely replaces the existing key's associated value. 
  * Keys must be "hashable" values. We won't define "hashable" right now. However, hashable values are usually (not always) immutable. All built-in immutable types (numbers, strings, booleans, tuples, frozen sets, and `None`) are hashable and can be dict keys. 
  * The values in each key/value pair may be any object. 


    
    
    d = {'a': 1, (1, 3): 3, 1: 'x'}
    print(d)         # {'a': 1, (1, 3): 3, 1: 'x'}
    print(d['a'])    # 1
    print(d[(1, 3)]) # 3
    print(d[1])      # 'x'
    
    d['a'] = 'A'
    print(d)        # {'a': 'A', (1, 3): 3, 1: 'x'}
    

Since version 3.7, Python dicts maintain the insertion order of the pairs. Python guarantees it. Thus, you can iterate over the pairs in the same order they were inserted into the dictionary. However, this behavior doesn't fundamentally alter whether dicts are unordered collections. In practice, you should mentally think of dicts as unordered collections, but it's OK to rely on the ordering in contexts where the insertion order matters.
    
    
    d = {'a': 1, (1, 3): 3, 1: 'x'}
    
    del d['a']      # Deletes key/value pair 'a': 1
    print(d)        # {(1, 3): 3, 1: 'x'}
    
    d['a'] = 42
    print(d)        # {(1, 3): 3, 1: 'x', 'a': 42}
    

## Sequence Constructors

Most built-in Python data types let the programmer create new objects using literal values. Literals are great. However, you can also use special functions called **constructors** to create new objects. In fact, sometimes you can't use literals; you must use constructors to create ranges, frozen sets, and empty sets.

Let's examine the constructors used with collections.

### String Constructor

The string constructor, `str`, has two basic formats, `str()` and `str(something)`, where `something` is any Python object. Regardless of what you pass to `str`, it returns a string. For instance:
    
    
    str()            # returns '' (empty string)
    str('abc')       # returns 'abc'
    str(42)          # returns '42'
    str(3.141592)    # returns '3.141592'
    str(False)       # returns 'False'
    str(None)        # returns 'None'
    str(range(3, 7)) # returns 'range(3, 7)'
    str([1, 2, 3])   # returns '[1, 2, 3]'
    str(int)         # returns "<class 'int'>"
    str(list)        # returns "<class 'list'>"
    
    class Person: pass
    str(Person())
    # returns "<__main__.Person object at 0x1006d21e0>"
    

In most cases, the values returned by `str` give a good idea of the original value. However, the last 6 lines show that the return value isn't always helpful. This is especially true with custom types like the `Person` class above (we'll learn about custom types in the [OO Python book](/books/oo_python)). You can fix this issue with custom types, but we won't discuss that until later in the Core Curriculum.

### Range Constructor

The `range` constructor comes in 3 forms:

  * `range(start, stop, step)`

This constructor generates a sequence of integers between `start` and `stop - 1` with an increment of `step` between each consecutive integer. You can use a negative step to generate a sequence in reverse order. In this case, the range ends at `stop + 1`. For instance:
    
        r = range(5, 12, 2)
    print(list(r))            # [5, 7, 9, 11]
    
    r = range(12, 8, -1)
    print(list(r))            # [12, 11, 10, 9]
    
    r = range(12, 5, -2)
    print(list(r))            # [12, 10, 8, 6]
    

You can create empty ranges by giving values where `start >= stop` when `step` is positive or `start <= stop` when `step` is negative. Empty ranges are often bugs.
    
        r = range(5, 5, 1)
    print(list(r))           # []
    
    r = range(5, 7, -1)
    print(list(r))            # []
    

  * `range(start, stop)`

When you omit the `step` argument, Python uses a default value of `1`. Hence, `range(start, stop)` is identical to `range(start, stop, 1)`.

  * `range(stop)`

When you omit the `start` argument, Python uses a default value of `0` for `start`. Hence, `range(stop)` is identical to `range(0, stop, 1)`.




Ranges are **lazy sequences** : they don't create any element values until your program needs them. This is why we use `list(r)` above; without it, `print(r)` prints something like `range(5, 12, 2)`, which may not be helpful. You can also use the `tuple` constructor to do the same thing. The `set` and `frozenset` constructors also work, but the sets may not be in the same order.

### The List, Tuple, Set, and Frozen Set Constructors

Lists, tuples, sets, and frozen sets share two common constructor forms:

  * `list()` or `list(iterable)`
  * `tuple()` or `tuple(iterable)`
  * `set()` or `set(iterable)`
  * `frozenset()` or `frozenset(iterable)`



The constructors with no arguments create an empty list, tuple, set, or frozen set, as appropriate: a sequence or set with no members.

The constructors that take an `iterable` argument expect an object that Python can iterate: an **iterable**. From the built-in types, the iterables include all sequences, strings, sets, and mappings. (Note that iterating a mapping iterates the mapping's keys.) Thus, you can use these constructors to convert lists to tuples, tuples to sets, strings to lists, and so on:
    
    
    my_str = 'Python'
    
    my_list = list(my_str)
    print(my_list)  # ['P', 'y', 't', 'h', 'o', 'n']
    
    my_tuple = tuple(my_list)
    print(my_tuple) # ('P', 'y', 't', 'h', 'o', 'n')
    
    my_set = set(my_tuple)
    print(my_set)   # {'t', 'o', 'n', 'h', 'P', 'y'}
    

You can also use these constructors to duplicate a collection:
    
    
    my_list = [5, 12, 2]
    another_list = list(my_list)
    
    print(my_list)                          # [5, 12, 2]
    print(another_list)                     # [5, 12, 2]
    
    print(my_list == another_list)          # True
    print(my_list is another_list)          # False
    

As you can see in lines 4, 5, and 7, the lists are identical. However, line 8 shows that the list objects are not the same object.

Let's look at a more complex example involving nested lists:
    
    
    my_list = [[1, 2, 3], [4, 5, 6]]
    another_list = list(my_list)
    
    print(my_list)                          # [[1, 2, 3], [4, 5, 6]]
    print(another_list)                     # [[1, 2, 3], [4, 5, 6]]
    
    print(my_list == another_list)          # True
    print(my_list is another_list)          # False
    print(my_list[0] is another_list[0])    # True
    print(my_list[1] is another_list[1])    # True
    

In this case, we can see from lines 4, 5, and 7 that the lists have the same values, and from line 8, we can see that they are different objects. Strangely, in lines 9 and 10, we can see that their elements **are** the same objects. That's because the `list` constructor performs what is known as a shallow copy. In a later chapter, we'll discuss shallow and deep copies and what is happening here. For now, remember that nested collections are subject to shallow copies. That's often fine. However, it can lead to problems that are difficult to diagnose.

Passing a string to any of these constructors causes it to iterate over the characters in the string. It places each character in a separate element of the resulting collection:
    
    
    print(tuple('Python'))
    # ('P', 'y', 't', 'h', 'o', 'n')
    

## Summary

Python has a rich variety of collections for storing and manipulating data. You'll see collections in almost all real-world programs; nearly every useful program uses them. We'll continue to explore them in the next chapter.

##  Exercises

  1. If you have a list named `people`, how can you determine the number of entries in that list?

#### Solution

You can use `len(people)` to determine the number of entries.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Can you write some code to change the value `'bye'` in the following tuple to `'goodbye'`?
    
        stuff = ('hello', 'world', 'bye', 'now')
    

Note: this problem is a bit tricky.

#### Solution

Since tuples are immutable, you can't replace `'bye'` with `'goodbye'`. At best, you can create a new tuple and reassign it:
    
        stuff = ('hello', 'world', 'goodbye', 'now')
    
    
        stuff = stuff[0:2] + ('goodbye', stuff[3])
    
    
        stuff = list(stuff)
    stuff[2] = 'goodbye'
    stuff = tuple(stuff)
    

Solution 1 creates an entirely new tuple with the changed value. That's not quite in the spirit of what we're asking. It would also be tedious if the tuple contained more than a few elements.

Solution 2 is a little closer to being in the proper spirit. This one concatenates a slice of the original tuple combined with a new tuple that includes `'goodbye'` and `'now'` (from `stuff[3]`). However, that code is difficult to read. Furthermore, the slicing and indexing is a sure-fire way to get an off-by-one error. For example, if you wrote `stuff[0:1]` instead of `stuff[0:2]`, the result would be missing `'world'`.

Solution 3 is as close as we can get to the spirit of the problem. Here, we convert the original tuple to a list and reassign the element to the new value. Finally, we transform the list into a new tuple. This approach still creates an entirely new tuple. However, it avoids the problem of re-entering a long list of members, is cleaner than slicing and indexing, and is much easier to read.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

#### Solution

     * Differences 
       1. Lists are mutable; tuples are immutable. 
       2. List literals use `[]`; tuple literals use `()`. 
     * Similarities 
       1. Lists and tuples are both sequences. Sequences are ordered collections that can use numeric indexes to access the members. 
       2. Lists and tuples are heterogeneous; elements do not need to all be the same type. 

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Why can we treat strings as sequences?

#### Solution

Strings are ordered; you can access the individual characters with indexing.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. How do the set types differ from the sequence types?

#### Solution

Sets are unordered; they don't support indexing.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. Assuming you have the following assignment:
    
        pi = 3.141592
    

Write some code that converts the value of `pi` to a string and assigns it to a variable named `str_pi`.

#### Solution
    
        pi = 3.141592
    str_pi = str(pi)
    
    
        pi = 3.141592
    str_pi = f'{pi}'
    

Solution 1 is the preferred solution since it is slightly more readable. Solution 2 works, too. However, f-strings are better suited for creating strings mixed with other text.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. Without running the following code, identify the numbers that are included in each of the following ranges:
    
        range(7)
    range(1, 6)
    range(3, 15, 4)
    range(3, 8, -1)
    range(8, 3, -1)
    

#### Solution
    
        range(7)            # [0, 1, 2, 3, 4, 5, 6]
    range(1, 6)         # [1, 2, 3, 4, 5]
    range(3, 15, 4)     # [3, 7, 11]
    range(3, 8, -1)     # []
    range(8, 3, -1)     # [8, 7, 6, 5, 4]
    

The most important thing to observe here is that ranges never include the "stop" value. Furthermore, a negative step value counts downwards from the start to the stop value. Thus, the start value should typically be larger than the stop value when the step value is negative.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. How would you print all the numbers in the following range?
    
        range(3, 17, 4)
    

#### Solution
    
        print(list(range(3, 17, 4)))
    
    
        print(tuple(range(3, 17, 4)))
    

Since ranges are lazy sequences, you must either iterate over the range or convert the range to a non-lazy sequence: a list or tuple. Here, we transform the range into a list and a tuple.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  9.     my_list = [1, 2, 3, [4, 5, 6]]
    another_list = list(my_list)
    

Given the above code, answer the following questions and explain your answers:

    1. Are the lists assigned to `my_list` and `another_list` equal? 
    2. Are the lists assigned to `my_list` and `another_list` the same object? 
    3. Are the nested lists at index 3 of `my_list` and `another_list` equal? 
    4. Are the nested lists at index 3 of `my_list` and `another_list` the same object? 

**Don't write any code for this exercise.**

#### Solution

    1. The two lists are **equal** : they are both lists with the same elements. 
    2. The two lists are **not the same** object: The `list` constructor creates a new object. 
    3. The two nested lists are **equal** : they are both lists that have the same elements. 
    4. The two nested lists are the **same** object: the `list` constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied. 

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  10. Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.
    
        names = { 'Chris', 'Clare', 'Karis', 'Karl',
              'Max', 'Nick', 'Victor' }
    print(names)
    

#### Solution

This code probably won't print the names alphabetically. Sets, by definition, are unordered collections. Thus, the order in which members are shown when printing or iterating is arbitrary. Bob's code may print the names alphabetically on rare occasions, but it would do so only once every 5040 times.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  11. Consider the data in the following table:

Name | Country  
---|---  
Alice | USA  
Francois | Canada  
Inti | Peru  
Monika | Germany  
Sanyu | Uganda  
Yoshitaka | Japan  
  
You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

#### Solution
    
        countries = {
        'Alice':     'USA',
        'Francois':  'Canada',
        'Inti':      'Peru',
        'Monika':    'Germany',
        'Sanyu':     'Uganda',
        'Yoshitaka': 'Japan',
    }
    
    print(countries['Monika'])
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Using Collections

In this chapter, we'll learn how to work with Python's collections. In particular, we'll explore indexing and key-based access, then explore some of the many operations most collections have in common.

## Indexing

Indexing is the process of using a whole number to access and perhaps alter an element of a sequence. All sequences, including strings, support indexing. Python uses index `0` as the first element of all built-in sequences. To access the first element of a sequence assigned to variable `seq`, we use `seq[0]`. We use `seq[1]` to access the second element. This process repeats until we exhaust the sequence:
    
    
    seq = ('a', 'b', 'c')
    print(seq[0])  # a (1st element)
    print(seq[1])  # b (2nd element)
    print(seq[2])  # c (3rd element)
    print(seq[3])  # IndexError: tuple index out of range
    

In the above example, we used a tuple as our sequence. However, we could have used any other sequence, such as a list or string. It's worth noting that the index of the final element is one less than the sequence's length.

An error occurred when accessing index 3. The last element in a 3-element sequence has index 2, not 3. The `len` function can determine a sequence's length. You can use its return value to determine whether an index is _out of range_ :
    
    
    seq = ('a', 'b', 'c')
    if len(seq) > 3:
        print(seq[3])
    

Note that we tested whether the length was greater than the intended index. If you want to access element 3, the sequence must have at least four elements.

Suppose we want to access the last element in a sequence? To do that, we can compute the index of the last element and then use that value:
    
    
    seq = ('a', 'b', 'c')
    last_index = len(seq) - 1
    print(seq[last_index])        # c
    

You can also use negative indexes, which are often easier to work with:
    
    
    seq = ('a', 'b', 'c')
    print(seq[-1])  # c (last element)
    print(seq[-2])  # b (next to last element)
    print(seq[-3])  # a (2nd to last element)
    

If you want to change the value of an element in a mutable sequence (i.e., a list), you can use indexing on the left side of an assignment:
    
    
    seq = ['a', 'b', 'c']
    seq[1] = 'B'
    print(seq)      # ['a', 'B', 'c']
    

This operation mutates the list but merely reassigns `seq[1]`.

## Slicing

The indexing syntax also supports a **slicing** augmentation. Slicing can extract (or modify) any number of consecutive elements simultaneously. For instance, the syntax `seq[start:stop]` retrieves the elements from `seq` whose index is between `start` and `stop - 1`, inclusive. You can also use negative indexes for the slice. Finally, you can use the `seq[start:stop:step]` syntax to slice every "step-th" element.
    
    
    seq = 'abcdefghi'
    print(seq[3:7])       # defg
    print(seq[-6:-2])     # defg
    print(seq[2:8:2])     # ceg
    print(repr(seq[3:3])) # ''
    print(seq[:])         # abcdefghi
    print(seq[::-1])      # ihgfedcba
    
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(seq[3:7])       # [4, 5, 6, 7]
    print(seq[-6:-2])     # [5, 6, 7, 8]
    print(seq[2:8:2])     # [3, 5, 7]
    print(seq[3:3])       # []
    print(seq[:])         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(seq[::-1])      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    seq = [[1, 2], [3, 4]]
    seq_dup = seq[:]
    print(seq[0] is seq_dup[0])   # True
    

Line 5 shows that you get an empty slice when the start and stop values are the same.

Line 6 returns a duplicate of the sequence. It is equivalent to `seq[0:len(seq)]`. This syntax creates a shallow copy, which we'll discuss later.

Line 7 returns a reversed copy of a sequence. `seq[::-1]` is similar to `seq.reverse()` (described later). The former returns a new sequence; the latter mutates the original. `seq.reverse()` is much easier to read, but the mutation should be intentional.

Lines 9-15 demonstrate that slicing also works with other sequences (a list in this case).

Lines 17-19 demonstrate that slicing performs a shallow copy if the sequence contains any collections, such as lists or tuples. Custom objects, which we'll meet in our [Object Oriented Programming with Python](/books/oo_python) book, are also subject to shallow copying.

Slicing also works as an assignment's target (the left side of an `=`). However, we'll refrain from demonstrating that as it often leads to code that is hard to read.

## Key-Based Access

Indexing uses whole numbers and only works with sequences and strings. However, mappings use a syntax called **key-based access** that looks like indexing. However, keys are usually strings, though not always.

Instead of limiting ourselves to whole numbers, we can use any hashable object as a key, which includes the built-in immutable types. We sometimes use integer keys, which, confusingly, look like indexing. Other types are rarely used but can be helpful (especially tuples).

With dicts, we use key-based access like this:
    
    
    my_dict = {
        'a': 'abc',
        37: 'def',
        (5, 6, 7): 'ghi',
        frozenset([1, 2]): 'jkl',
    }
    
    print(my_dict['a'])                # abc
    print(my_dict[37])                 # def
    print(my_dict[(5, 6, 7)])          # ghi
    print(my_dict[frozenset([1, 2])])  # jkl
    print(my_dict['nothing'])     # KeyError: 'nothing'
    

We've used a string, an integer, a tuple, and a frozen set as keys in this dict. We've also seen that we get a `KeyError` if we try to use a non-existent key. If there's a chance you might get a `KeyError`, consider using the `dict.get` method. It returns the value associated with a given key if the key exists. Otherwise, it produces a default return value (usually `None`, but other values can be specified):
    
    
    my_dict = {
        'a': 'abc',
        37: 'def',
        (5, 6, 7): 'ghi',
        frozenset([1, 2]): 'jkl',
    }
    
    print(my_dict.get('a'))                 # abc
    print(my_dict.get('nothing'))           # None
    print(my_dict.get('nothing', 'N/A'))    # N/A
    print(my_dict.get('nothing', 100))      # 100
    

We can also use key-based access to the left of the `=` operator:
    
    
    my_dict = {
        'a': 'abc',
        37: 'def',
        (5, 6, 7): 'ghi',
        frozenset([1, 2]): 'jkl',
    }
    
    my_dict['a'] = 'ABC'
    my_dict[37] = 'DEF'
    my_dict[(5, 6, 7)] = 'GHI'
    my_dict[frozenset([1, 2])] = 'JKL'
    print(my_dict)
    # Pretty printed for clarity
    # {
    #     'a': 'ABC',
    #     37: 'DEF',
    #     (5, 6, 7): 'GHI',
    #     frozenset({1, 2}): 'JKL'
    # }
    

Can we assign new keys to a dict?
    
    
    my_dict['xyz'] = 'Hey there!'
    print(my_dict['xyz'])         # Hey there!
    

By all means, we can!

Can we use a mutable key?
    
    
    my_dict[[1, 2, 3]] = 'Hey there!'
    # TypeError: unhashable type: 'list'
    

Nope. It doesn't work. Dictionary keys must be immutable.

## Common Collection Operations

Most Python collections support various operations, functions, and methods, some of which only apply to mutable collections. We'll examine the non-mutating operations first. We won't cover everything you can do. However, we'll see most of what you will encounter at Launch School.

### Non-Mutating Operations for Collections

All of the operations in this section work equally well with mutable and immutable collections. They never modify the original collection. Instead, they return new objects.

#### Collection Membership

The `in` operator determines whether the object to the operator's left is in the iterable collection on the right. It returns `True` if the item on the left is in the collection on the right, `False` otherwise.

The `not in` operator is the inverse of `in`. It returns `False` if the object is in the collection; `True` if not.

With sequences and sets, these operators compare the object for equality against each collection element. For mappings (dicts), it checks whether the item is a key in the dictionary. For strings, it determines whether the right string contains the left string.
    
    
    seq = [4, 'abcdef', (True, False, None)]
    print(4 in seq)                         # True
    print(4 not in seq)                     # False
    print('abcdef' in seq)                  # True
    print('abcdef' not in seq)              # False
    print('cde' in seq[1])                  # True
    print('cde' not in seq[1])              # False
    print('acde' in seq[1])                 # False
    print('acde' not in seq[1])             # True
    print((True, False, None) in seq)       # True
    print((True, False, None) not in seq)   # False
    print(3.14 in seq)                      # False
    print(3.15 not in seq)                  # True
    

#### Minimum and Maximum Members

`min` and `max` return the minimum and maximum members in an iterable collection. The only requirement is that any pair of the collection's elements are comparable with the `<` and `>` operators.
    
    
    my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
    my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}
    
    print(min(my_set1), max(my_set1))     # -63 25
    print(min(my_set2), max(my_set2))     # -1 4
    

As you can see, `min` and `max` know how to compare the members of our sets. It determines the type of comparison by looking at the element types.

In most cases, you can't use `min` and `max` with heterogenous collections:
    
    
    >>> my_set = {1, 4, '-9', 16, '25', -36, -63, -1}
    >>> min(my_set)
    TypeError: '<' not supported between instances of
    'str' and 'int'
    
    >>> max(my_set)
    TypeError: '>' not supported between instances of
    'str' and 'int'
    

However, it is possible in some situations:
    
    
    my_set = {1, 3.14, -2.71}
    print(min(my_set), max(my_set))      # -2.71 3.14
    

You can also use `min` and `max` with multiple arguments instead of an iterable.
    
    
    print(min(3, 5, -1), max(3, 5, -1))  # -1 5
    

#### Summation

The `sum` function is used in conjunction with iterable collections that consist entirely of numeric values. It computes and returns the sum of all the collection's numbers.
    
    
    numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
    print(sum(numbers))                       # 88
    

Despite what Python's [official documentation](https://docs.python.org/3/library/functions.html#sum) says, `sum` cannot be used with strings. It only works with numeric types. Use `str.join` if you want to concatenate strings

#### Locating Indices and Counting

Two helpful sequence methods are the `index` and `count` methods. `seq.index` returns the index of the first element in the sequence that matches a given object. It raises a `ValueError` exception if the object is not found. `seq.count` returns the number of times a value occurs in the sequence.
    
    
    names = ['Karl', 'Grace', 'Clare', 'Victor',
             'Antonina', 'Allison', 'Trevor']
    print(names.index('Clare'))   # 2
    print(names.index('Trevor'))  # 6
    print(names.index('Chris'))
    # ValueError: 'Chris' is not in list
    
    
    
    numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
    print(numbers.count(1))       # 2
    print(numbers.count(3))       # 1
    print(numbers.count(4))       # 4
    print(numbers.count(7))       # 0
    

`index` also works with strings. It searches for the first matching substring of a string:
    
    
    names = 'Karl Grace Clare Victor Antonina Trevor'
    print(names.index('Clare'))   # 11
    print(names.index('Trevor'))  # 33
    print(names.index('Chris'))
    # ValueError: substring not found
    

#### Merging Collections

One of the most impressively helpful functions is `zip`, which works with all iterables. It lets you merge the members of multiple iterables into a single list of tuples. `zip` makes it easy to iterate through many collections simultaneously.

`zip` iterates through 0 or more iterables in parallel and returns a list-like object of tuples. Each tuple contains a single object from each of the iterables. That's a mouthful, so let's take a look at an example:
    
    
    iterable1 = [1, 2, 3]
    iterable2 = ('Kim', 'Leslie', 'Bertie')
    iterable3 = [None, True, False]
    
    zipped_iterables = zip(iterable1, iterable2, iterable3)
    print(list(zipped_iterables))
    # Pretty printed for clarity
    # [
    #   (1, 'Kim', None),
    #   (2, 'Leslie', True),
    #   (3, 'Bertie', False)
    # ]
    

Here, we've combined 3 iterables (two lists and a tuple) into a list-like object of tuples. Each tuple in the return value has 3 members. The first member is from `iterable1`, the second from `iterable2`, and the third from `iterable3`. The first tuple contains the first element of each of the iterables, the second tuple contains the second element of the iterables, and the third tuple contains the third element. Thus, our first tuple contains the first elements of `iterable1` (1), `iterable2` ('Kim'), and `iterable3` (None).

Note that we referred to `zip`s return value as a _list-like object_. It's not a true list, but a lazy sequence much the same as a `range`. You must request values explicitly, which you can do with a loop or iterable constructor. That's why we call `list(zipped_iterables)` on line 6 above.

`zip`'s collection arguments are usually the same length but don't have to be. If you want to enforce identical lengths, add a `strict=True` keyword argument to the invocation:
    
    
    zipped_iterables = zip(iterable1, iterable2, strict=True)
    

With `strict=True`, `zip` raises an exception if the iterables don't all have the same length.

So, what happens if the lengths differ and `strict=True` isn't given? In this case, `zip` stops after exhausting the shortest iterable:
    
    
    result = zip(range(5, 10),    # length is 5
                 range(1, 3),     # length is 2 (shortest)
                 range(3, 7))     # length is 4
    print(list(result)) # [(5, 1, 3), (6, 2, 4)]
    

Since `range(1, 3)` only has a length of 2 and `strict=True` was omitted, the `result` list only has 2 elements.

The `zip` function's canonical application is to simultaneously iterate over multiple collections. We'll demonstrate that in the next chapter.

It's worth noting that `zip` returns what is known as an _iterator_. We'll discuss iterators in more detail in the Core curriculum. However, one characteristic of iterators that is important to be aware of is that they can only be _consumed_ once. If you iterate over the iterator object, subsequent attempts to iterate will fail. For instance:
    
    
    result = zip(range(5, 10),    # length is 5
                 range(1, 3),     # length is 2 (shortest)
                 range(3, 7))     # length is 4
    print(list(result)) # [(5, 1, 3), (6, 2, 4)]
    print(list(result)) # []
    

As you can see, once we've consumed the return value of `zip`, we can't do it again. Most Python functions and methods that return lazy sequences may only be consumed once; `range` objects are one of the few exceptions to this rule.

#### Operations on Dictionaries

Python provides 3 methods to get lists of the keys, values, and key/value pairs from a dictionary. Those methods are `dict.keys`, `dict.values`, and `dict.items`. Let's see them in action:
    
    
    people_phones = {
        'Chris': '111-2222',
        'Pete':  '333-4444',
        'Clare': '555-6666',
    }
    
    print(people_phones.keys())
    # dict_keys(['Chris', 'Pete', 'Clare'])
    
    print(people_phones.values())
    # Pretty printed for clarity
    # dict_values([
    #     '111-2222',
    #     '333-4444',
    #     '555-6666'
    # ])
    
    print(people_phones.items())
    # Pretty printed for clarity
    # dict_items([
    #     ('Chris', '111-2222'),
    #     ('Pete',  '333-4444'),
    #     ('Clare', '555-6666')
    # ])
    

The lists produced by these methods aren't ordinary lists. Python wraps the output for each list with `dict_keys()`, `dict_values()`, or `dict_items()` to show that these aren't regular lists. They are actually **dictionary view objects** that are tied to the dictionary. If you add a new key/value pair to the dictionary, remove an element, or update a value, the corresponding lists are updated immediately:
    
    
    people_phones = {
        'Chris': '111-2222',
        'Pete':  '333-4444',
        'Clare': '555-6666',
    }
    
    keys = people_phones.keys()
    values = people_phones.values()
    
    print(keys)    # dict_keys(['Chris', 'Pete', 'Clare'])
    print(values)
    # dict_values(['111-2222', '333-4444', '555-6666'])
    
    people_phones['Max'] = '123-4567'
    people_phones['Pete'] = '345-6789'
    del people_phones['Chris']
    
    print(keys)    # dict_keys(['Pete', 'Clare', 'Max'])
    print(values)
    # dict_values(['345-6789', '555-6666', '123-4567'])
    

### Operations for Mutable Sequences

Let's see some of the mutating operations we can use with mutable sequences, the most common of which are lists. All methods in this section mutate the collection used to call them.

Keep in mind that all these methods work with any properly defined mutable sequence, such as deques and arrays, both of which are available for Python.

#### Adding Elements to Mutable Sequences

We can use the `append`, `insert`, and `extend` methods to add new elements to a mutable sequence, such as a list.

  * `seq.append` appends a single object to the end of a mutable sequence, such as a list:
    
        numbers = [1, 2]
    
    numbers.append(10)      # Append the number 10
    print(numbers)          # [1, 2, 10]
    

  * `seq.insert` inserts an object into a mutable sequence before the element at a given index. If the given index is greater than or equal to the sequence's length, the object is appended to the sequence. If the index is negative, it is counts from the end of the sequence.
    
        numbers = [1, 2]
    
    numbers.insert(0, 8)    # Insert 8 before numbers[0]
    print(numbers)          # [8, 1, 2]
    numbers.insert(2, 6)    # Insert 6 before numbers[2]
    print(numbers)          # [8, 1, 6, 2]
    numbers.insert(100, 55) # Insert 55 before numbers[100]
    print(numbers)          # [8, 1, 6, 2, 55]
    numbers.insert(-3, 33)  # Insert 33 before the 3rd element
                            # from the end.
    print(numbers)          # [8, 1, 33, 6, 2, 55]
    

  * `seq.extend` appends the contents of an iterable sequence to the calling iterable sequence.
    
        numbers = [1, 2]
    
    numbers.extend([7, 8])  # Append 7 and 8 to numbers
    print(numbers)          # [1, 2, 7, 8]
    




#### Removing Elements from Mutable Sequences

We can use the `remove`, `pop`, and `clear` methods to remove elements from a mutable sequence:

  * `seq.remove` searches a sequence for a specific object and removes the first occurrence of that object. It raises a `ValueError` if there is no such object.
    
        my_list = [2, 4, 6, 8, 10]
    
    my_list.remove(8)
    print(my_list)            # [2, 4, 6, 10]
    
    my_list.remove(8)
    # ValueError: list.remove(x): x not in list
    

  * `seq.pop` removes and returns an indexed element from a mutable sequence. If no index is given, it removes the last element in the sequence. It raises an error if the index is out of range. `pop` only works with mutable _indexed_ sequences.
    
        my_list = [2, 4, 6, 8, 10]
    
    print(my_list.pop(1))         # 4
    print(my_list)                # [2, 6, 8, 10]
    
    print(my_list.pop())          # 10
    print(my_list)                # [2, 6, 8]
    
    print(my_list.pop(4))
    # IndexError: pop index out of range
    

  * `seq.clear` removes all elements from a sequence, leaving it empty.
    
        my_list = [2, 4, 6, 8, 10]
    
    my_list.clear()
    print(my_list)                # []
    




### Sorting Collections

You can use the `sorted` function to create a sorted list from any iterable collection, mutable or immutable. It creates and returns a sorted list from the elements in the collection. The original collection is unchanged.

You can also sort lists using the `list.sort` method. However, this method mutates the list. It's also worth noting that `my_list.sort()` is a bit faster and less memory intensive than `sorted(my_list)` since the method does an in-place sort, so doesn't have to build a completely new list.
    
    
    names = ('Grace', 'Clare', 'Allison', 'Trevor')
    print(sorted(names))
    # ['Allison', 'Clare', 'Grace', 'Trevor']
    
    print(names)
    # ('Grace', 'Clare', 'Allison', 'Trevor')
    
    names = list(names)
    print(names)
    # ['Grace', 'Clare', 'Allison', 'Trevor']
    
    print(names.sort())   # None
    print(names)
    # ['Allison', 'Clare', 'Grace', 'Trevor']
    

In the `sorted` example, we've sorted and printed the tuple of names. Note that the result is a list, not a tuple. We've then shown that the original `names` tuple is unchanged.

Next, we converted the `names` tuple to a list and sorted it with `names.sort`. Note that `sort` returned `None`, which strongly hints that the collection was mutated. When we print the names, we see that the list was mutated.

By default, both `sort` and `sorted` do an ascending sort using the `<` operator to compare elements from the collection. You can reverse the sort by adding a `reverse=True` **keyword argument** to the argument list:
    
    
    names = ['Grace', 'Clare', 'Allison', 'Trevor']
    print(sorted(names, reverse=True))
    # ['Trevor', 'Grace', 'Clare', 'Allison']
    
    names.sort(reverse=True)
    print(names) # ['Trevor', 'Grace', 'Clare', 'Allison']
    

You can also pass a `key=func` keyword argument to tell `sort` or `sorted` how to determine what values it should sort. For instance, if you want to perform a case-insensitive sort on a list of strings, you can specify `key=str.casefold`:
    
    
    words = ['abc', 'DEF', 'xyz', '123']
    print(sorted(words))
    # ['123', 'DEF', 'abc', 'xyz']
    
    print(sorted(words, key=str.casefold))
    # ['123', 'abc', 'DEF', 'xyz']
    

In most cases, you can also use `str.lower` instead of `str.casefold`. However, using `str.casefold` is considered best-practice since `sort` will be comparing the strings.

You can also sort a list of numeric-valued strings by passing `key=int` to the function or method:
    
    
    numbers = ['1', '5', '100', '15', '534', '53']
    numbers.sort()
    print(numbers)   # ['1', '100', '15', '5', '53', '534']
    
    numbers.sort(key=int)
    print(numbers)   # ['1', '5', '15', '53', '100', '534']
    

This is probably your first time seeing that Python's functions and methods are objects that can be passed around as arguments to a function. (They can also be passed around as return values.) Remember this moment. The technique is potent.

If you use `sorted` on a dictionary, it returns a sorted list of the dictionaries keys.

#### Reversing Sequences and Dictionaries

You can use the `reversed` function to reverse the order of elements in a sequence or dictionary. The returned value is a lazy sequence that contains the elements in the sequence or the keys from a dictionary. Since the result is lazy, you need to iterate over the result or expand it with a function list `list` or `tuple`.

You can also reverse lists using the `list.reverse` method. However, this method mutates the list. In general, you should use `list.reverse` when you really need to reverse the list's contents, and don't need to preserve the original order. You should use `reversed` when all you need to do is iterate over the list in reverse. Don't use `reversed` if you eventually want to convert the result to a non-lazy sequence such as a list or tuple:
    
    
    names = ('Grace', 'Clare', 'Allison', 'Trevor')
    reversed_names = reversed(names)
    print(reversed_names)
    # <reversed object at 0x102848e50>
    print(tuple(reversed(names))) # Requires extra memory
    # ('Trevor', 'Allison', 'Clare', 'Grace')
    print(names)
    # ('Grace', 'Clare', 'Allison', 'Trevor')
    
    names = list(names)
    print(names.reverse())   # None
    print(names)
    # ['Trevor', 'Allison', 'Clare', 'Grace']
    
    my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
    reversed_dict = reversed(my_dict)
    print(reversed_dict)
    # <dict_reversekeyiterator object at 0x100d19f80>
    
    print(list(reversed_dict))    # Requires extra memory
    # ['jkl', 'pqr', 'xyz', 'abc']
    

In the `reversed` example using a tuple, we've reversed and printed the tuple of names. We've then shown that the original `names` tuple is unchanged.

Next, we converted the `names` tuple to a list and reversed it with `names.reverse`. Note that `reverse` returned `None`, which strongly hints that the collection was mutated. When we print the names, we see that the list was mutated.

Finally, we demonstrated using `reversed` with a dictionary.

Think of the `reversed` function as a looping aid. You sometimes want to iterate over a collection in reverse. `reversed` makes that easy:
    
    
    names = ('Grace', 'Clare', 'Allison', 'Trevor')
    for name in reversed(names):
        print(name)
    # Trevor
    # Allison
    # Clare
    # Grace
    

## String Operations

As we've seen, Python has many built-in functions for manipulating sequences and other collections. You can use many of these functions with strings, even though strings are not proper collections or sequences.

The `str` class also offers a veritable goldmine of methods for using and manipulating strings in myriad ways. Let's take a look at some of these. We cannot cover them all, but we'll look at some of the most useful. We'll skip over anything we've already discussed in any detail.

### Letter Case

We've already seen how the `str.lower` and `str.upper` methods work. Let's check out two related methods:

  * `str.capitalize` returns a copy of `str` with the first character capitalized and the remaining characters converted to lowercase.
    
        print("what's up?".capitalize())        # What's up?
    print('456ABC'.capitalize())            # 456abc
    

  * `str.title` returns a copy of `str` with every word in the string capitalized. The remaining characters are converted to lowercase.
    
        print("four SCORE and sEvEn".title())
    # Four Score And Seven
    

`str.title` idea of what constitutes a word can lead to unexpected results. In particular, it uses whitespace and certain punctuation characters as word boundaries:
    
        print("i can't believe it's already mid-july.".title())
    # I Can'T Believe It'S Already Mid-July.
    

If you only want to break at whitespace, you can use the `capwords` function from the `string` module:
    
        import string
    print(string.capwords("i can't believe it's already mid-july."))
    # I Can't Believe It's Already Mid-july.
    

  * `str.swapcase` returns a copy of `str` with every uppercase letter converted to lowercase, and vice versa.
    
        print("What's up?".swapcase())          # wHAT'S UP?
    print('456ABC'.swapcase())              # 456abc
    print('456ABC'.swapcase().swapcase())   # 456ABC
    

The first call to `swapcase` on line 3 returns the original string with the case swapped; the second swaps the case on that return value.

Note that there are situations where `str.swapcase().swapcase()` does not return the original value of `str`. For instance:
    
        print('Straße'.swapcase().swapcase())   # Strasse
    

In this case, the German eszet character (`ß`), which represents a doubled lowercase `s` (`ss`), does not have an uppercase counterpart. Thus, the above example prints `Strasse` instead of `Straße`.




### Character Classification

Python has a generous suite of methods that test what sort of characters are present in a string. We'll look at just a few of these -- there are many more.

  * `str.isalpha()` returns `True` if all characters of `str` are alphabetic, `False` otherwise. It returns `False` if the string is empty.
    
        'Hello'.isalpha()      # True
    'Good-bye'.isalpha()   # False: `-` is not a letter
    'Four score'.isalpha() # False: space is not a letter
    ''.isalpha()           # False
    

  * `str.isdigit()` returns `True` if all characters of `str` are digits, `False` otherwise. It returns `False` if the string is empty.
    
        '12340'.isdigit()      # True
    '123.4'.isdigit()      # False: `.` is not a digit
    '-1234'.isdigit()      # False: `-` is not a digit
    ''.isdigit()           # False
    

  * `str.isalnum()` returns `True` if `str` is composed entirely of letters and/or digits, `False` otherwise. It returns `False` if the string is empty.

  * `str.islower()` returns `True` if all cased characters in `str` are lowercase letters, `False` otherwise. It returns `False` if the string contains no case characters.

  * `str.isupper()` returns `True` if all cased characters in `str` are uppercase, `False` otherwise. It returns `False` if the string contains no case characters.

  * `str.isspace()` returns `True` if all characters in `str` are **whitespace characters** , `False` otherwise. It returns `False` if the string is empty. The whitespace characters include ordinary spaces (``), tabs (`\t`), newlines (`\n`), and carriage returns (`\r`). It also includes two rarely used characters: vertical tabs (`\v`) and form feeds (`\f`), as well as some foreign characters that count as whitespace.




Be careful with these methods: they're all Unicode-aware. Thus, `'Καλωσήρθες'.isalpha()` returns `True` since the characters are all part of the Greek alphabet. If you need to exclude non-ASCII characters, use this pattern:
    
    
    text.isalpha() and text.isascii()
    

### Stripping Characters

The `str.strip` method returns a copy of `str` with all leading and trailing whitespace characters (see `str.isspace` above) removed. Python programmers often use this method to strip unwanted whitespace from input data, such as keyboard input. Unwanted whitespace frequently makes input data harder to work with, so immediately removing excess whitespace is a good idea.
    
    
    text = input(prompt).strip()
    

In some of the examples in this section, we use the built-in `repr` function when printing strings. `repr` formats strings with quotes and clearly shows the presence of whitespace characters:
    
    
    text = ' \t  abc def    \n\r'
    print(repr(text))             # ' \t  abc def    \n\r'
    print(repr(text.strip()))     # 'abc def'
    

You can also tell `strip` to remove other characters by providing a string argument. The characters inside this string are the ones you want removed.
    
    
    text = ' \t  abc def    \n\r'
    print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'
    
    text = 'aaabaacccabxyzabccba'
    print(text.strip('a'))         # baacccabxyzabccb
    print(text.strip('ab'))        # cccabxyzabcc
    print(text.strip('ba'))        # cccabxyzabcc
    print(text.strip('abc'))       # xyz
    print(text.strip('bc'))        # aaabaacccabxyzabccba
    
    print(repr(text.strip('abcxyz'))) # ''
    

There are things to note with the above examples:

  * Lines 2 and 9 show that only leading and trailing characters that match the argument are removed. 
  * Lines 6-8 show that `strip` removes individual characters, not substrings. That is, the order of the characters in the argument doesn't matter. Thus, on line 8, we remove all of the leading and trailing `'a'`, `'b'`, and `'c'` characters, leaving nothing but `'xyz'`. 



The `str.lstrip` method is identical to `str.strip` except it only removes leading characters (the leftmost). Similarly, `str.rstrip` removes trailing characters (the rightmost).
    
    
    text = 'aaabaacccabxyzabccba'
    
    print(text.lstrip('a'))       # baacccabxyzabccba
    print(text.rstrip('a'))       # aaabaacccabxyzabccb
    
    print(text.lstrip('ab'))      # cccabxyzabccba
    print(text.rstrip('ab'))      # aaabaacccabxyzabcc
    
    print(text.lstrip('ba'))      # cccabxyzabccba
    print(text.rstrip('ba'))      # aaabaacccabxyzabcc
    
    print(text.lstrip('abc'))     # xyzabccba
    print(text.rstrip('abc'))     # aaabaacccabxyz
    

### startswith and endswith

Two related methods are available for determining whether a string begins or ends with a given substring. Let's examine these methods:

  * `str.startswith` returns `True` if the string given by `str` begins with a certain substring, `False` if it does not:
    
        'Four score and seven'.startswith('Four score')  # True
    'Four score and seven'.startswith('For score')   # False
    'Four score and seven'.startswith('score')       # False
    

The argument can also be a tuple of strings:
    
        'abc def'.startswith(('abc', 'xyz', 'stu'))  # True
    'def ghu'.startswith(('abc', 'xyz', 'stu'))  # False
    'xyz uvw'.startswith(('abc', 'xyz', 'stu'))  # True
    'stu vwx'.startswith(('abc', 'xyz', 'stu'))  # True
    

The method also accepts "start" and "end" indexes to control where the search begins and ends:
    
        'abc def'.startswith('def', 4)           # True
    'abc def ghi'.startswith('def', 4, 7)    # True
    

  * `str.endswith` returns `True` if the string given by `str` ends with a certain substring, `False` if it does not:
    
        'Four score and seven'.endswith('and seven')  # True
    'Four score and seven'.endswith('ad seven')   # False
    'Four score and seven'.endswith('score')      # False
    

As with `startswith`, the argument can be a tuple of strings. You can also supply "start" and "end" indexes:
    
        'abc def'.endswith(('abc', 'xyz', 'stu'))  # False
    'abc def'.endswith(('xyz', 'def'))         # True
    'abc def'.endswith('def', 4)               # True
    'abc def ghi'.endswith('def', 4, 7)        # True
    




### Splitting and Joining Strings

The `str.split` method returns a list of the words in the string `str`. By default, `split` splits the string at sequences of one or more whitespace characters:
    
    
    text = '  Four     score and   seven years ago.   '
    print(text.split())
    # ['Four', 'score', 'and', 'seven', 'years', 'ago.']
    
    print('no-spaces'.split()) # ['no-spaces']
    

If you want to split on something other than spaces, you can tell Python what character or character string should act as a delimiter:
    
    
    text = ',Four,score,and,,,seven,years,ago,'
    print(text.split(','))
    # Pretty printed for clarity
    # [
    #     '',
    #     'Four',
    #     'score',
    #     'and',
    #     '',
    #     '',
    #     'seven',
    #     'years',
    #     'ago',
    #     ''
    # ]
    

Note that specifying a delimiter changes the splitting behavior. Instead of looking for runs of whitespace, it splits the string at every occurrence of the delimiter. This also applies when using a literal space character as the delimiter. Compare the output of the code below to our first example:
    
    
    text = '  Four     score and   seven years ago.   '
    print(text.split(' '))
    # Partially pretty printed for clarity
    # ['', '', 'Four', '', '', '', '', 'score', 'and',
    #  '', '', 'seven', 'years', 'ago.', '', '', '']
    

`split` also recognizes multi-character delimiters:
    
    
    text = 'Four<>score<:>and<>seven<>years<>ago'
    print(text.split('<>'))
    # ['Four', 'score<:>and', 'seven', 'years', 'ago']
    

Multi-character delimiters must match exactly. Thus, the `<` and `>` in `<:>` aren't split.

Most major languages have a `split` function or method. It's worth noting that Python's differs from most others in that you can't split a string into individual characters using `split`. Python's `str.split` method doesn't allow a separator of ''. If you need to split a string into characters, use the `list` or `tuple` function:
    
    
    text = 'abcde'
    print(list(text))             # ['a', 'b', 'c', 'd', 'e']
    print(tuple(text))            # ('a', 'b', 'c', 'd', 'e')
    

You can also iterate strings a character at a time:
    
    
    text = 'abcde'
    for char in text:
        print(char)
    

`str.splitlines` returns a list of lines from the string `str`. `splitlines` looks for line-ending characters like `\n` (line feed), `\r` (carriage return), `\n\r` (new lines), and a variety of other line boundaries. See the documentation for a complete list.
    
    
    text = '''
    You were lucky to have a room. We used to have to
    live in a corridor.
    Oh we used to dream of livin' in a corridor!
    Woulda' been a palace to us. We used to live in an
    old water tank on a rubbish tip. We got woken up
    every morning by having a load of rotting fish
    dumped all over us.
    '''
    
    print(text.strip().splitlines())
    # Pretty printed for clarity
    [
        "You were lucky to have a room. We used to have to",
        "live in a corridor.",
        "Oh we used to dream of livin' in a corridor!",
        "Woulda' been a palace to us. We used to live in an",
        "old water tank on a rubbish tip. We got woken up",
        "every morning by having a load of rotting fish",
        "dumped all over us."
    ]
    

The final method we'll discuss in this cluster is `str.join`, which concatenates all strings in an iterable collection into a single lone string. Each string from the collection gets concatenated to the previous string with the value of `str` between them:
    
    
    words = ['You', 'were', 'lucky']
    print(''.join(words))         # Youwerelucky
    print(' '.join(words))        # You were lucky
    print(','.join(words))        # You,were,lucky
    print('\n  '.join(words))
    # You
    #   were
    #   lucky
    

### Finding Substrings

We often need to search through strings looking for a particular substring. Python provides several ways to do this, including the `in` and `not in` operators we looked at earlier.

Here, we'll look at the `str.find` and `str.rfind` methods. `str.find` searches through `str` looking for the first occurrence of the argument. `str.rfind` does the same, but it searches from right to left (that is, in reverse). Both methods return the index of the first matching substring. Otherwise, they return `-1`.
    
    
    school = 'launch school'
    
    print(school.find(' '))       # 6
    print(school.find('l'))       # 0
    print(school.find('h'))       # 5
    print(school.find('hoo'))     # 9
    print(school.find('x'))       # -1
    print(school.find('N'))       # -1
    
    print(school.rfind(' '))      # 6
    print(school.rfind('l'))      # 12
    print(school.rfind('h'))      # 9
    print(school.rfind('hoo'))    # 9
    print(school.rfind('oh'))     # -1
    print(school.rfind('N'))      # -1
    

Note that both `find` and `rfind` are case sensitive, so `'N'` doesn't match `'n'`.

You can also search slices by adding start and end arguments to the invocation:
    
    
    text = 'abc abc def abc'
    
    print(text.find(' ', 4))         # 7
    print(text.find(' ', 8))         # 11
    
    print(text.find('c', 0, 2))      # -1
    print(text.rfind('c', 3, 10))    # 6
    

Using `find` or `rfind` to search slices is not the same as using the `[start:stop]` syntax first and then searching the result. Compare the outputs for the two `find` invocations below:
    
    
    text = 'abc abc def abc'
    
    print(text[3:10].find('c'))     # 3
    print(text.find('c', 3, 10))    # 6
    

If you take a slice of a string before using it to call `find` or `rfind`, the method returns the index of the search string in that slice. However, the method considers the starting index when you use the slicing arguments. Another difference is that taking a slice first creates a new string, while using slicing arguments does not.

## Nested Collections

Collections can be nested inside other collections. For instance, you can have a list that contains a dict, a set, a tuple, and another list. Each of those can, in turn, also contain nested collections:
    
    
    nested_list = [
        {'foo': 42, 'bar': [1, 2, 3], 'qux': None},
        {
            'Kim',
            ('Leslie', 'Les'),
            ('Pete', 'Peter'),
            ('Jonathan', 'Jon', 'Jack'),
        },
        (4, 5, (1, 2, 3), 6, 7),
        ['a', 'b', 'cde', -3.141592],
    ]
    

There are, however, some limitations on what you can nest in certain collections. For instance, in most cases, you can't nest mutable collections inside some collections. For instance, you can't nest a mutable collection such as a list, dictionary, or another set inside a set:
    
    
    >>> my_set = {1, 2, 3, [4, 5]}
    TypeError: unhashable type: 'list'
    
    >>> my_set = {1, 2, 3, {4, 5}}
    TypeError: unhashable type: 'set'
    

However, you can nest a frozen set inside a set or frozen set:
    
    
    >>> my_set = { 1, 2, 3, frozenset([4, 5]) }
    >>> my_set          # {frozenset({4, 5}), 1, 2, 3}
    

Curiously, you can nest mutable collections inside tuples even though tuples are immutable.
    
    
    >>> my_tuple = (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})
    >>> my_tuple
    (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})
    

In most cases, nested collections have some sense of structure and reason for the nesting. For instance, we might define a deck of cards as a list of dictionaries:
    
    
    deck = [
        { 'suit': 'Clubs', 'value': '2' },
        { 'suit': 'Clubs', 'value': '3' },
        { 'suit': 'Clubs', 'value': '4' },
            ...
        { 'suit': 'Spades', 'value': 'Queen' },
        { 'suit': 'Spades', 'value': 'King' },
        { 'suit': 'Spades', 'value': 'Ace' },
    ]
    

If we want to print the fiftieth card in the deck, we can write:
    
    
    print(f"{deck[49]['value']} of {deck[49]['suit']}")
    # Queen of Spades
    

You can also have several layers of nesting in a sequence. In that case, you can access any item from any nested part of the sequence by just running several `[]` indexing operations together:
    
    
    nested_seq = [
        [1, 2, [3, 4, (5, 6, 7, 8)]],
        [9, [10, (11,)]],
        [12, 13, [14, 15, (16, 17)]],
        [18, [19, 20, (21, 22)]],
    ]
    
    print(nested_seq[1])          # [9, [10, (11,)]]
    print(nested_seq[3][0])       # 18
    print(nested_seq[0][2][2])    # (5, 6, 7, 8)
    print(nested_seq[2][2][2][1]) # 17
    

Nested collections become really "_fun_ " when you start having to iterate through them.

## Comparing Collections

As you might expect, Python supports comparison operations for collections. It provides comparison mechanisms for all built-in iterable collections, and you can define comparisons for any custom iterables you create.

Equality is the most straightforward comparison. If two iterables meet all of the following requirements, they are equal. Otherwise, they are unequal.

  * They have the same type: (list, tuple, set, etc.) Note that sets and frozen sets are considered the same for comparison purposes. 
  * They have the same number of elements. 
  * For sequences, each pair of corresponding elements compares as equal. 
  * For sets, each set has the same members (order doesn't matter). 
  * For mappings, each key/value pair must be present and identical in both mappings (order doesn't matter). 


    
    
    print([2, 3] == [2, 3])    # True
    print([2, 3] == [3, 2])    # False (diff sequence)
    print([2, 3] == [2])       # False (diff lengths)
    print([2, 3] == (2, 3))    # False (diff types)
    print({2, 3} == {3, 2})    # True (same members)
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 2, 'a': 1}
    dict3 = {'a': 1, 'b': 2, 'c': 3}
    
    print(dict1 == dict2)      # True (same pairs)
    print(dict1 == dict3)      # False
    

Of course, you can also use `!=` to compare for inequality.

You can also compare sequences for `<`, `<=`, `>`, and `>=`. However, we won't go into that here. It's rarely needed.

## Summary

Python's collections have a wealth of functions, methods, and other operations that programmers need daily. Sometimes, the most challenging problem is deciding whether you need a function, a method, or an operator.

##  Exercises

  1. Write Python code to print the seventh number of `range(0, 25, 3)`.

#### Solution
    
        my_range = range(0, 25, 3)
    print(my_range[6])                      # 18
    
    
        print(range(0, 25, 3)[6])               # 18
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Use slicing to write Python code to print a 6-character substring of `'Launch School'` that begins with the first `c`.

#### Solution
    
        my_str = 'Launch School'
    print(my_str[4:10])                   # ch Sch
    

The first `c` occurs at index 4, so that's our start value for the slice. Since we want 6 characters, the stop value is at index 4 + 6 or 10. Note that the character at index 10 is not included in the result.

If you want to determine the location of the substring programmatically, you can do this:
    
        my_str = 'Launch School'
    start = my_str.find('c')
    print(my_str[start:start + 6])        # ch Sch
    

Some error checking might be advisable there.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Write Python code to create a new tuple from `(1, 2, 3, 4, 5)`. The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple `(4, 3, 2)`.

#### Solution
    
        my_tuple = (1, 2, 3, 4, 5)
    my_list = list(my_tuple)
    my_list.reverse()
    result = tuple(my_list[1:4])
    print(result)       # (4, 3, 2)
    
    
        my_tuple = (1, 2, 3, 4, 5)
    result = my_tuple[3:0:-1]
    print(result)       # (4, 3, 2)
    
    
        my_tuple = (1, 2, 3, 4, 5)
    result = my_tuple[-2:-5:-1]
    print(result)       # (4, 3, 2)
    

There are several ways to solve this problem. Your first inclination may have been to use the `reverse` method, as in Solution 1. However, `reverse` only works with lists, so we must first convert the tuple to a list. Even so, we have to slice the list, though the slice is a little cleaner.

Solutions 2 and 3 use the same approach by extracting a reversed slice. The only difference is how we specify the start and stop values for the slice. What makes these tricky is that the element indexed by the stop value is not included in the result. If you used one of these solutions, you likely started with an off-by-one bug.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. This is a 3-part question. Consider the following dictionary:
    
        pets = {
        'Cat':  'Meow',
        'Dog':  'Bark',
        'Bird': 'Tweet',
    }
    

     * **Part 1** : Write some code to print `Bark` by accessing the element associated with the key `Dog`. 
     * **Part 2** : Write some code to print `None` when you try to print the value associated with the non-existent key, `Lizard`. 
     * **Part 3** : Write some code to print `<silence>` when you try to print the value associated with the non-existent key, `Lizard`. 

#### Solution
    
        print(pets['Dog'])
    
    
        print(pets.get('Lizard'))
    
    
        print(pets.get('Lizard', '<silence>'))
    

Since the `pets` dictionary doesn't have a `Lizard` key, we need to use the `dict.get` method so we don't get an error. In Part 2, we don't specify a default value, so `get` returns `None`. In Part 3, we set `<silence>` as the default value.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. Which of the following values **can't** be used as a key in a `dict` object, and why?
    
        'cat'
    (3, 1, 4, 1, 5, 9, 2)
    ['a', 'b']
    {'a': 1, 'b': 2}
    range(5)
    {1, 4, 9, 16, 25}
    3
    0.0
    frozenset({1, 4, 9, 16, 25})
    

#### Solution

The following items can't be used as keys:
    
        ['a', 'b']
    {'a': 1, 'b': 2}
    {1, 4, 9, 16, 25}
    

The first value is a list, the second another dict, and the last a set. Since all 3 types are mutable, they can't be used as dict keys. All remaining items are immutable built-in objects; they are acceptable dict keys.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. What will the following code print?
    
        print('abc-def'.isalpha())
    print('abc_def'.isalpha())
    print('abc def'.isalpha())
    print('abc def'.isalpha() and
          'abc def'.isspace())
    print('abc def'.isalpha() or
          'abc def'.isspace())
    print('abcdef'.isalpha())
    print('31415'.isdigit())
    print('-31415'.isdigit())
    print('31_415'.isdigit())
    print('3.1415'.isdigit())
    print(''.isspace())
    

#### Solution
    
        print('abc-def'.isalpha())       # False
    print('abc_def'.isalpha())       # False
    print('abc def'.isalpha())       # False
    print('abc def'.isalpha() and
          'abc def'.isspace())       # False
    print('abc def'.isalpha() or
          'abc def'.isspace())       # False
    print('abcdef'.isalpha())        # True
    print('31415'.isdigit())         # True
    print('-31415'.isdigit())        # False
    print('31_415'.isdigit())        # False
    print('3.1415'.isdigit())        # False
    print(''.isspace())              # False
    

There are two things to note above.

     * **Lines 4-7** : You can't use `and` or `or` to determine whether a string contains a mixture of different value types. The `str.isXXXXX` methods determine whether every character in `str`matches a certain class of characters. Thus, a string can't be both alphabetic and whitespace. It can be alphabetic or whitespace, but that doesn't work for something like `'abc def'`. 
     * **Line 13** : Most of the `str.isXXXXX` methods return `False` when invoked by an empty string. 

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. Write Python code to replace all the `:` characters in the string below with `+`.
    
        info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
    

Try this problem using the methods you've learned about in this chapter. Once you have that working, use the Python documentation for the `str` type to find an alternative solution.

#### Solution
    
        info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
    parts = info.split(':')
    result = '+'.join(parts)
    print(result)
    # 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'
    
    
        info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
    result = info.replace(':', '+')
    print(result)
    # 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. Explain why the code below prints different values on lines 3 and 4.
    
        text = "It's probably pining for the fjords!"
    
    print(text[21:35].rfind('f'))     # 8
    print(text.rfind('f', 21, 35))    # 29
    

#### Solution

Line 3 first extracts a slice from `text` ranging from index 21 through index 35. That returns the string `'for the fjords'`. `rfind` then returns `8`, the index of the rightmost instance of an `'f'`.

On the other hand, line 4 does a search for the rightmost `f` between indexes 21 and 35. Since the `f` occurs at index 29, that's what the method returns.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  9. Write some code to replace the value `6` in the following nested list with `606`:
    
        stuff = [
        ['hello', 'world'],
        ['example', 'mem', None, 6, 88],
        [4, 8, 12],
    ]
    

You don't have to search the list. Just write an assignment that replaces the `6`.

#### Solution
    
        stuff[1][3] = 606
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  10. Consider the following nested collection:
    
        cats = {
        'Pete': {
            'Cheddar': {
                'color': 'orange',
                'enjoys': {
                    'sleeping',
                    'snuggling',
                    'meowing',
                    'eating',
                    'birdwatching',
                },
            },
            'Cocoa': {
                'color': 'black',
                'enjoys': {
                    'eating',
                    'sleeping',
                    'playing',
                    'chewing',
                },
            },
        },
    }
    

Write one line of code to print the activities that Cocoa enjoys.

#### Solution
    
        print(cats['Pete']['Cocoa']['enjoys'])
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  11. Without running the following code, determine what each line should print.
    
        print('johnson' in 'Joe Johnson')
    print('sen' not in 'Joe Johnson')
    print('Joe J' in 'Joe Johnson')
    print(5 in range(5))
    print(5 in range(6))
    print(5 not in range(5, 10))
    print(0 in range(10, 0, -1))
    print(4 in {6, 5, 4, 3, 2, 1})
    print({1, 2, 3} in {1, 2, 3})
    print({3, 2} in {1, frozenset({2, 3})})
    

#### Solution
    
        print('johnson' in 'Joe Johnson')      # False
    print('sen' not in 'Joe Johnson')      # True
    print('Joe J' in 'Joe Johnson')        # True
    print(5 in range(5))                   # False
    print(5 in range(6))                   # True
    print(5 not in range(5, 10))           # False
    print(0 in range(10, 0, -1))           # False
    print(4 in {6, 5, 4, 3, 2, 1})         # True
    print({1, 2, 3} in {1, 2, 3})          # False
    print({3, 2} in {1, frozenset({2, 3})}) # True
    

     * **Line 1** : `in` with strings is case sensitive. 
     * **Line 4** : `range(5)` does not include `5`; it ranges from 0 to 4. 
     * **Line 7** : `range(10, 0, -1)` does not include `0`; it ranges from 10 to 1. 
     * **Line 9** : `in` with sets only checks whether a specific value is in the set. 
     * **Line 10** : `{3, 2}` and `frozenset({2, 3})` are considered equal sets. 

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  12. Write some code that determines and prints whether the number `3` appears inside each of these lists:
    
        numbers1 = [1, 3, 5, 7, 9, 11]
    numbers2 = []
    numbers3 = [2, 4, 6, 8]
    numbers4 = ['1', '3', '5']
    numbers5 = ['1', 3.0, '5']
    

You should print `True` or `False` depending on each result.

#### Solution
    
        print(3 in numbers1)          # True
    print(3 in numbers2)          # False
    print(3 in numbers3)          # False
    print(3 in numbers4)          # False (3 != '3')
    print(3 in numbers5)          # True  (3 == 3.0)
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  13. Without running the following code, determine what each print statement should print.
    
        cats = ('Cocoa', 'Cheddar',
            'Pudding', 'Butterscotch')
    print('Butterscotch' in cats)
    print('Butter' in cats)
    print('Butter' in cats[3])
    print('cheddar' in cats)
    

#### Solution
    
        cats = ('Cocoa', 'Cheddar',
            'Pudding', 'Butterscotch')
    print('Butterscotch' in cats) # True
    print('Butter' in cats)       # False (note 1)
    print('Butter' in cats[3])    # True (note 2)
    print('cheddar' in cats)      # False
    

     * **Note 1** : "string `in` list" must match a list element exactly. 
     * **Note 2** : `cats[3]` is `'Butterscotch'` and `'Butter'` is in `'Butterscotch'`. 

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  14. Assume you have the following sequences:
    
        my_str = 'abc'
    my_list = ['Alpha', 'Bravo', 'Charlie']
    my_tuple = (None, True, False)
    my_range = range(10, 60, 10)
    

Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values, which should look like this:
    
        [('a', 'Alpha', None, 10),
     ('b', 'Bravo', True, 20),
     ('c', 'Charlie', False, 30)]
    

#### Solution
    
        result = zip(my_str, my_list, my_tuple, my_range)
    print(list(result))
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  15. Without running the following code, what values will be printed by line 10?
    
        pets = {
        'Cat':  'Meow',
        'Dog':  'Bark',
        'Bird': 'Tweet',
    }
    
    keys = pets.keys()
    del pets['Dog']
    pets['Snake'] = 'Sssss'
    print(keys)
    

#### Solution
    
        dict_keys(['Cat', 'Bird', 'Snake'])
    

Since `dict.keys` returns a dictionary view object, any changes made to the dictionary after you call the `keys` method will be reflected in dictionary view referenced by `keys` immediately.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Loops and Iterating

Most programs require code that runs repeatedly. Such code runs while a given condition remains truthy or until it becomes falsy (they mean the same thing). Most programming languages, including Python, use loops to provide this capability.

Python loops have several forms, but the main looping structures are the `for` and `while` statements. These loops execute a block repeatedly while a condition remains truthy. You can also think of the loop running until the condition becomes falsy. Both mental models are equivalent.

Python has three other looping mechanisms: comprehensions, generators, and functional loops. We'll talk about comprehensions in this chapter. However, we'll postpone the discussion of generators and functional loops to a later course in the Core Curriculum.

Let's begin with the **while loop**.

## while Loops

A `while` loop uses the `while` keyword followed by a conditional expression, a colon (`:`), and a block. The loop repeatedly executes the block while the conditional expression remains truthy. In most programs, that loop should ultimately stop repeating. That means the block must do something to help Python know when to stop. That is, it must arrange to terminate the loop. That's usually triggered by evaluating a conditional expression. Otherwise, the loop is an **infinite loop** that never stops repeating.

To see why a `while` loop is useful, consider writing some code that prints numbers from 1 to 10:
    
    
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
    

While that code is straightforward and readily understood, it's easy to see why this approach is unsustainable. Suppose we need to print the numbers from 1 to 1000 or 1,000,000. If you had to write all that code for such a simple task, you would soon regret your career choice.

Let's rewrite the program with a `while` loop. Create a file named `counter.py` with the following code and run it:
    
    
    counter = 1
    while counter <= 10:
        print(counter)
        counter += 1
    

This code does the same thing as the first program but more programmatically. It **iterates** over the block for all integer values between 1 and 10, inclusive. Each time the block runs is called an **iteration**.

If you want to print 1000 numbers or even a million, all you have to change is the conditional expression:
    
    
    counter = 1
    # highlight
    while counter <= 1000:
    # endhighlight
        print(counter)
        counter += 1
    

Go ahead and run the code now using the command line:
    
    
    python counter.py
    

When Python encounters this `while` loop, it evaluates the conditional expression, `counter <= 1000`. Since `counter`'s initial value is `1`, the expression is initially `True`, so Python executes the block. We print `counter`'s value inside the block, then increment it by `1`.

After the first iteration, Python re-evaluates the conditional expression. This time, `counter` is `2`, which is still less than or equal to `1000`; thus, the block runs again. After 1000 iterations, `counter`'s value becomes 1001. Since the loop condition is no longer truthy, the program stops looping. It continues with the first expression or statement after the loop.

**Line 4 in this example is crucial**. The block _must_ modify `counter` somehow, ultimately making the loop condition falsy. If it doesn't, the loop never ends, which is usually not what you want. If your program never stops running, you probably have an infinite loop somewhere in the program. Try commenting out line 4 and rerun the code. You'll see that it continually prints the number `1`. You can use the `Control+c` keystroke to terminate the program.

Go ahead and uncomment line 4.

### Using while Loops with Sequences

One of the most common uses of loops in programming is to iterate over a sequence's elements and perform some action on each element. For example, we may want to iterate over a list of names and create a new list that contains the names in uppercase. Here's one way to do that:
    
    
    names = ['Chris', 'Max', 'Karis', 'Victor']
    upper_names = []
    index = 0
    
    while index < len(names):
        upper_name = names[index].upper()
        upper_names.append(upper_name)
        index += 1
    
    print(upper_names);
    # ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
    

A bit of explanation is in order here. The variable `names` holds a list of names. We want to append each name, in uppercase, to the initially empty `upper_names` list. Since list indexes are zero-based, we initialize an `index` variable with `0`.

Next, we use a loop that executes as long as the number in `index` is smaller than the length of the `names` list. Line 8 increments the index by `1` after each iteration, which ensures that `index < len(names)` becomes falsy after the loop handles the last element.

Line 6 accesses the name stored at `names[index]` and uses it to call `str.upper`. That method returns the name in uppercase, which we assign to `upper_name`. It doesn't change the original name in the `names` list.

Line 7 uses `list.append` to append the latest uppercase name to the `upper_names` list. Over the four iterations of the `names` list, line 7 appends four uppercase names to `upper_names`, one per iteration, in the same order the loop processes them.

Notice that we initialized `names`, `upper_names`, and `index` before the loop. We don't want to initialize them inside the loop; they would get reset during every iteration. Basically, nothing would change. That wouldn't work well even if the code ran without error.

## for Loops

`for` loops have the same purpose as `while` loops, but they use a condensed syntax that works well when iterating over lists and other sequences. A `for` loop lets you forget about indexing your sequences. You don't have to initialize or increment the index value or even need a condition. Moreover, `for` loops work on all built-in collections (including strings). Most loops you write in Python will be `for` loops.
    
    
    for element in collection:
        # loop body: do something with the element
    

If `collection` is a sequence, this structure behaves in much the same way as:
    
    
    index = 0
    while index < len(collection):
        # loop body
        # do something with collection[index]
        index += 1
    

The `for` loop is more elegant and significantly less error-prone.

Let's rewrite `names.py` with a `for` loop to better illustrate using `for`:
    
    
    names = ['Chris', 'Max', 'Karis', 'Victor']
    upper_names = []
    
    # highlight
    for name in names:
    # endhighlight
        upper_name = name.upper()
        upper_names.append(upper_name)
        # highlight
        # Deleted: index += 1
        # endhighlight
    
    print(upper_names);
    # ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
    

The result is the same as with the `while` loop. However, the code is much easier to read and maintain.

For illustrative purposes, let's see what happens when we use a `for` loop to iterate over a string:
    
    
    for char in 'Launch School':
        print(char)
    
    
    
    L
    a
    u
    n
    c
    h
    
    S
    c
    h
    o
    o
    l
    

If you want to work with words instead of characters, you can use the `split` method:
    
    
    for word in 'Launch School'.split():
        print(word)
    
    
    
    Launch
    School
    

You can also use `for` loops with other collections, such as sets and dicts. Any iterable collection, in fact:
    
    
    # Looping over a set
    my_set = {1000, 2000, 3000, 4000, 5000}
    for member in my_set:
        print(member)
    
    
    
    # The output may not be in this sequence since it
    # comes from a set.
    4000
    2000
    5000
    3000
    1000
    
    
    
    # Looping over a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key in my_dict:
        print(key)
    
    
    
    a
    b
    c
    

Using a `for` loop with a `dict` iterates over the `dict` keys by default. If you want the values or pairs, you can request them with the `values` or `items` methods:
    
    
    # Looping over a dictionary's values
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for value in my_dict.values():
        print(value)
    
    
    
    1
    2
    3
    
    
    
    # Looping over a dictionary's key/value pairs
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for item in my_dict.items():
        print(item)
    
    
    
    ('a', 1)
    ('b', 2)
    ('c', 3)
    

A more Pythonic way to iterate over both the keys and values simultaneously is to use tuple unpacking:
    
    
    # Looping over a dictionary's key/value pairs
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for (key, value) in my_dict.items():
        print(f'{key} = {value}')
    
    
    
    a = 1
    b = 2
    c = 3
    

We'll cover tuple unpacking in the Core Curriculum. For now, all you need to know is that each key returned by the `items` method gets assigned to the `key` variable, and each associated value gets assigned to the `value` variable.

By the way: you don't need the parentheses around `key, value`. The following code works and is more Pythonic:
    
    
    # Looping over a dictionary's key/value pairs
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in my_dict.items():
        print(f'{key} = {value}')
    

### Nested Loops

You will often need to nest loops within one or more outer loops. For instance, suppose you want to create a deck of cards given two lists: the suits and ranks you want to combine:
    
    
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace',
    ]
    
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f'{rank} of {suit}'
            deck.append(card)
    
    print(deck)
    

With nested `for` loops, you start with the outer loop and assign the variable to the first element of its collection (`suit` and `suits`). You then process the inner loop in its entirety. Here, we match the first suit with every possible card rank, appending each card to the deck.

Once the inner loop finishes processing, control returns to the outer loop. Working with the second element of the outer loop's collection, it again iterates over the inner loop's collection. This continues until all members of the outer loop's collection have been processed. In our card deck example, the outer loop runs 4 times, while the inner loop runs 4 * 13 (52) times.

Nesting 3 or more levels deep is possible but frequently inadvisable. Too much nesting is hard to understand. Using one or more helper functions to handle the more deeply nested processing is often a good idea.

You can also nest `while` loops and mix `for` and `while` loops.

## Controlling Loops

Python uses the keywords `continue` and `break` to provide more control over `for` and `while` loops. `continue` starts a new loop iteration; `break` terminates the loop early.

### Continuing a Loop With Next Iteration

Let's stick with the `names.py` program. Suppose we want all the uppercase names in our `upper_names` list except `'Max'`. The `continue` statement can help us do that.
    
    
    names = ['Chris', 'Max', 'Karis', 'Victor']
    upper_names = []
    
    for name in names:
        if name == 'Max':
            continue
    
        upper_name = name.upper()
        upper_names.append(upper_name)
    
    print(upper_names);
    # ['CHRIS', 'KARIS', 'VICTOR']
    

The result doesn't contain `'MAX'`.

When a loop encounters the `continue` keyword, it skips running the rest of the block and jumps ahead to the next iteration. In this example, we tell the loop to ignore `'Max'` and skip to the next iteration without adding `'MAX'` to `upper_names`.

You can often rewrite a loop that uses `continue` with a negated `if` conditional:
    
    
    names = ['Chris', 'Max', 'Karis', 'Victor']
    upper_names = []
    
    for name in names:
        if name != 'Max':
            upper_name = name.upper()
            upper_names.append(upper_name)
    
    print(upper_names);
    # ['CHRIS', 'KARIS', 'VICTOR']
    

This code behaves like the version that uses `continue` but is a little more concise.

Why bother using `continue` if we can write looping logic without it? You don't have to use `continue`, of course. However, it often leads to a more elegant solution to a problem. Without `continue`, your loops can get cluttered with nested conditional logic.
    
    
    for value in collection:
        if some_condition():
            # some code here
            if another_condition():
                # some more code here
    

We can use `continue` to rewrite this loop without the nested `if`s:
    
    
    for value in collection:
        if not some_condition():
            continue
    
        # some code here
    
        if not another_condition():
            continue
    
        # some more code here
    

Which of these is more readable and easier to maintain? That's not always easy to answer. As is often the case, the choice may be made for you by local coding standards. At other times, it's a matter of deciding which version looks and reads better.

The `continue` statement tells Python to start the next iteration of the nearest enclosing loop. You can't start a new iteration of an outer loop if you're currently in an inner (nested) loop.

### Breaking Out of a Loop

Instead of exiting the current iteration, you sometimes want to stop iterating completely. For instance, when you search a list for a specific value, you probably want to stop searching once you find it. There's no reason to keep searching if you don't need any subsequent matches.

Let's explore this idea with some code. Create a file named `search.py` with the following code and run it from your terminal:
    
    
    numbers = [3, 1, 5, 9, 2, 6, 4, 7]
    found_item = -1
    index = 0
    
    while index < len(numbers):
        if numbers[index] == 5:
            found_item = index
    
        index += 1
    
    print(found_item)
    

This program iterates over the elements of a list to find the element whose value is `5`. It saves the `index` value in `found_item`. However, the loop continues to iterate after finding the desired value. That seems pointless and wasteful. It's where `break` steps in and saves the day:
    
    
    numbers = [3, 1, 5, 9, 2, 6, 4, 7]
    found_item = -1
    index = 0
    
    while index < len(numbers):
        if numbers[index] == 5:
            found_item = index
            # highlight
            break
            # endhighlight
    
        index += 1
    
    print(found_item)
    

The `break` statement tells Python to terminate the nearest enclosing loop once we find the desired element. You can't break out of an outer loop if you're currently in an inner (nested) loop.

### Emulating Do/While Loops

A typical `while` loop looks something like this:
    
    
    while some condition is truthy
        do some work
    

In most code, this is a perfectly fine solution; you usually want to skip over the "do some work" part if "some condition" is initially falsy. However, sometimes you want to "do some work" at least once, even if the condition is initially falsy. For that, you need something like this:
    
    
    do some work
    while some condition is truthy
    

In other words, you always want to "do some work" at least once. This is often called a do/while or do/until loop since many languages have a looping structure with those names. Python does not, so you must take a different approach. That typically uses a `break` statement at the end of the loop, like so:
    
    
    do some work
        if some condition is falsy
            break
    

This often comes up in interactive programs where you may want to execute the main program loop at least once before exiting. The code to handle such a loop might look something like this:
    
    
    keep_going = True
    while keep_going:
        # main loop code is here
    
        answer = input('Play again? (y/n) ')
        if answer == 'n':
            keep_going = False
    

That's workable, albeit a little awkward. A slightly less clumsy alternative uses `break` and `while True`.
    
    
    while True:
        # main loop code is here
    
        answer = input('Play again? (y/n) ')
        if answer == 'n':
            break
    

## Simultaneous Iteration

We sometimes need to iterate through multiple collections in parallel. That is, we want to grab data from several collections during each loop iteration. If all the collections are indexed sequences, you can write a `while` loop using indexes. However, that's error-prone and often messy.

Meet the hero of parallel iteration: `zip`! The `zip` function is specifically designed to make simultaneous iteration easy. Let's see what this looks like.

Suppose you need to print the full names of several thousand people. For bizarre historical reasons, you have two lists: one contains the forenames, and the other contains the corresponding surnames. Without `zip`, you need to use a `while` loop and indexing. That's feasible, so let's try it. We'll use 4 names to test the concept:
    
    
    forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
    surnames = ['Camp', 'Blake', 'Flanagan', 'Short']
    
    index = 0
    while index < len(forenames):
        if index >= len(surnames): # surnames might be shorter.
            break
    
        forename = forenames[index]
        surname = surnames[index]
        print(f'{forename} {surname}')
    
        index += 1
    
    
    
    Ken Camp
    Lynn Blake
    Pat Flanagan
    Nancy Short
    

While it's not horrid, it's a lot of work. We can do better than that with `zip`:
    
    
    forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
    surnames = ['Camp', 'Blake', 'Flanagan', 'Short']
    
    zipped_names = zip(forenames, surnames)
    for forename, surname in zipped_names:
        print(f'{forename} {surname}')
    

That definitely looks better! However, we should explain lines 4 and 5. On line 4, `zip` creates a lazy sequence that acts like a list of tuples. Each tuple contains a forename and a surname. Line 5 is the start of our loop. We're taking advantage of the fact that `for` can assign multiple variables when the collection elements are tuples. Thus, we can grab the forename and surname from the current tuple.

Note that `zip` takes care of the potential problem of dealing with lists of different sizes. Our first attempt needed that `if` statement in the `while` block to guard against the `surnames` list being shorter than `forenames`.

## Comprehensions

Python supports a concise and readable way to create mutable collections from existing iterable collections: **comprehensions**. There are 3 comprehension types: list, dict, and set. Properly used, comprehensions can simplify your code and make it easier to understand.

Unlike most `for` and `while` loops, which are statements, comprehensions are expressions. You can use a comprehension on the right side of an assignment, as a function argument, as a return value, or any other place where you can use an expression that evaluates as a list, dict, or set. You can even use them as standalone expressions:
    
    
    [print(foo) for foo in collection]
    

However, an ordinary `for` loop is the preferred alternative.

### List Comprehensions

The most commonly used comprehensions are **list comprehensions**. They take an iterable collection and create a new list through iteration and optional selection. List comprehensions have the following format:
    
    
    [ expression for element in iterable if condition ]
    

The `if condition` portion is optional: it tells Python to select only certain elements from the `iterable`. The `for element in iterable` portion describes the iteration: it looks exactly like a `for` loop. It can be read in much the same way. Finally, the `expression` is a value that gets returned by each iteration of the loop. Python collects all the return values and puts them in a new list.

The `expression` in a comprehension often performs a **transformation**. It determines a new value based on an element from the original collection. Such comprehensions are called **transformations**.

If the `if condition` portion is present, we say that the comprehension also performs **selection**. With selections, it's not uncommon to return the original values from the collection:
    
    
    [ element for element in iterable if condition ]
    

The terms transformation and selection are handy to remember. You will encounter them in many languages.

Consider this basic example of a transformative list comprehension:
    
    
    squares = [ number * number for number in range(5) ]
    print(squares)      # [0, 1, 4, 9, 16]
    

Here, we're iterating over the numbers in the indicated range: `0, 1, 2, 3, 4`. We compute the square with `number * number` for each number. Finally, Python collects all the squares into a list and assigns the list to the `squares` variable. Voila! We now have a list of squares.

Of course, we could do the same thing with an ordinary `for` loop:
    
    
    squares = []
    for number in range(5):
        square = number * number
        squares.append(square)
    
    print(squares)      # [0, 1, 4, 9, 16]
    

That's quite a bit more code, and the effort of reading it is a bit higher.

Let's look at a selection example:
    
    
    multiples_of_6 = [ number for number in range(20)
                       if number % 6 == 0 ]
    print(multiples_of_6)      # [0, 6, 12, 18]
    

Here, we see the pattern of using the original collection values as the expression. We've also split the comprehension over two lines, which can aid readability.

This example combines selection and transformation:
    
    
    even_squares = [ number * number
                     for number in range(10)
                     if number % 2 == 0 ]
    print(even_squares)      # [0, 4, 16, 36, 64]
    

This code selects all of the even numbers in the specified range and then returns a list of the squares of the chosen numbers.

Let's try iterating over a dictionary. Suppose we have a dict of cats. We're using the cat names as keys; each name is associated with the cat's coat color. We want to create a list of the names in uppercase:
    
    
    cats_colors = {
        'Tess':   'brown',
        'Leo':    'orange',
        'Fluffy': 'gray',
        'Ben':    'black',
        'Kat':    'orange',
    }
    
    names = [ name.upper() for name in cats_colors ]
    print(names)
    # ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']
    

This is nearly identical to using the `dict.keys` method. The only difference is that the list comprehension returns an ordinary list, not a dictionary view object.

You can also iterate over the values by iterating `in cats_colors.values()` or the key/value pairs by iterating `in cats_colors.items()`.

Suppose we now want to limit the result list to just orange cats. We can accomplish that by adding a selection criterion to the comprehension:
    
    
    cats_colors = {
        'Tess':   'brown',
        'Leo':    'orange',
        'Fluffy': 'gray',
        'Ben':    'black',
        'Kat':    'orange',
    }
    
    names = [ name.upper()
              for name in cats_colors
              if cats_colors[name] == 'orange' ]
    print(names) # ['LEO', 'KAT']
    

It's also possible to use multiple selection criteria. Let's limit the result to cats whose name begins with `L`:
    
    
    cats_colors = {
        'Tess':   'brown',
        'Leo':    'orange',
        'Fluffy': 'gray',
        'Ben':    'black',
        'Kat':    'orange',
    }
    
    names = [ name.upper()
              for name in cats_colors
              if cats_colors[name] == 'orange'
              if name[0] == 'L' ]
    print(names) # ['LEO']
    

Multiple selection criteria act like nested `if` statements or as `and`-ed conditions. The selections combine, so only collection members matching all criteria are selected.

Comprehensions can also have multiple `for` loop components. For instance, let's generate a deck of cards based on a list of the suits and a list of the ranks:
    
    
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace',
    ]
    
    deck = [ f'{rank} of {suit}'
             for suit in suits
             for rank in ranks ]
    print(deck)
    

Compare this code with the one shown earlier in **Nested Loops**. As multiple selection criteria resemble a nested `if`, multiple looping components resemble a nested `for` loop.

### Dictionary Comprehensions

**Dictionary comprehensions** are almost identical to list comprehensions. However, they create new dictionaries instead of lists. Syntactically, they use curly braces instead of square brackets, and the expression becomes a "key: value" pair. Dictionary comprehensions have the following format:
    
    
    { key: value for element in iterable if condition }
    

The most significant difference is that the `expression` component is now a key/value pair, each given by another expression.

Consider this basic example of a dictionary comprehension:
    
    
    squares = { f'{number}-squared': number * number
                for number in range(1, 6) }
    print(squares)
    # pretty-printed for clarity.
    {
        '1-squared': 1,
        '2-squared': 4,
        '3-squared': 9,
        '4-squared': 16,
        '5-squared': 25
    }
    

Other than the differences mentioned above, list and dict comprehensions are identical.

### Set Comprehensions

**Set comprehensions** look almost identical to dict comprehensions. However, they create a new set instead of a dict and only have one expression to the left of the word `for`:
    
    
    { expression for element in iterable if condition }
    

Previously, a colon-separated key/value expression pair was to the left of `for`. Now, we only have an expression.

Consider this basic example of a set comprehension:
    
    
    squares = { number * number for number in range(1, 6) }
    print(squares)      # {1, 4, 9, 16, 25}
    

Other than the differences mentioned above, dict and set comprehensions are identical.

### Why No Tuple, Range, or String Comprehensions?

Python programmers often wonder why Python doesn't have tuple comprehensions. They can easily see that the following valid code hints that it might be a tuple comprehension:
    
    
    squares = ( number * number for number in range(1, 6) )
    print(squares) # <generator object <genexpr> at 0x104e39a40>
    

However, it is not a comprehension. Instead, it is a **generator** expression. We won't discuss generators in this book, but you'll see them later in the Core Curriculum. You'll also learn why they are helpful. The fact that a generator expression looks like it should be tuple comprehension is merely a matter of syntax. It doesn't answer the question of why.

Comprehensions don't build their results all at once. Each kind of comprehension works something like this:
    
    
    result = empty_collection               # [], {}, set()
    for item in collection:
        result.append(item)
    

As you can see, our `result` starts as an empty collection. We then modify the `result` collection during each iteration by appending a new item to `result`. From this, it's clear that the result must be a mutable type. Tuples are immutable, so Python can't have tuple comprehensions.

Since ranges and strings are also immutable, comprehensions can't create them. If you must have a tuple or string, use the `tuple` or `str` constructors to convert a list comprehension's result into a tuple or string. (Sorry, but you can't do something similar to create a range.)

## Summary

Loops and comprehensions are a great way to perform repeated operations on a collection. In Python, you'll often find yourself reaching for a comprehension before a loop, but not always. Let's test these concepts with some exercises!

##  Exercises

  1. The following code causes an infinite loop (a loop that never stops iterating). Why?
    
        counter = 0
    
    while counter < 5:
        print(counter)
    

#### Solution

The problem occurs in the loop body. We never increment `counter`, so `counter < 5` always returns a truthy value.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Modify the `age.py` program you wrote in Exercise 3 of the [Input/Output chapter](/books/python/read/input_output#exercises). The updated code should use a `for` loop to display the future ages.

#### Solution
    
        age = int(input('How old are you? '))
    print(f'You are {age} years old.')
    print()
    
    for future in range(10, 50, 10):
        print(f'In {future} years, you will be '
              f'{age + future} years old.')
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Use a `while` loop to print the numbers in `my_list`, one number per line. Then, do the same with a `for` loop.
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    
        6
    3
    0
    11
    20
    4
    17
    

#### Solution
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    index = 0
    while index < len(my_list):
        number = my_list[index]
        print(number)
        index += 1
    
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    for number in my_list:
        print(number)
    

Our solution using a `while` loop uses indexing to control iteration and to access the list members. Note that we start by setting `index` to `0` and then iterate while `index` is less than the list length.

The solution using a `for` loop is clearly easier to understand -- we don't have to mess around with indexing; we only need to iterate over the list elements.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Use a `while` loop to print all numbers in `my_list` with **even** values, one number per line. Then, print the **odd** numbers using a ' for' loop.
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    
        6
    0
    20
    4
    
    
        3
    11
    17
    

#### Solution
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    index = 0
    while index < len(my_list):
        number = my_list[index]
        # Even numbers are exactly divisible by 2
        if number % 2 == 0:
            print(number)
    
        index += 1
    
    
        my_list = [6, 3, 0, 11, 20, 4, 17]
    
    for number in my_list:
        # Odd numbers are not exactly divisible by 2
        if number % 2 != 0:
            print(number)
    

Our solutions both rely on using the `%` operator to determine whether a number is exactly divisible by 2. Even numbers are; odd numbers aren't. In both cases, we only need to compare the result of `element % 2` with `0`. If `number % 2` is `0`, the number is even. Otherwise, it is odd.

As with the previous problem, we needed indexing to control the `while` loop. However, the `for` loop led to code that is easier to read.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. Print all of the even numbers in the following list of nested lists. Don't use any `while` loops.
    
        my_list = [
        [1, 3, 6, 11],
        [4, 2, 4],
        [9, 17, 16, 0],
    ]
    
    
        6
    4
    2
    4
    16
    0
    

#### Solution
    
        my_list = [
        [1, 3, 6, 11],
        [4, 2, 4],
        [9, 17, 16, 0],
    ]
    
    for nested_list in my_list:
        for number in nested_list:
            if number % 2 == 0:
                print(number)
    

That may not have been too easy. Nested loops are hard to think about, but you'll encounter them often enough to have dreams about them. We start by iterating over the nested lists inside `my_list`. That means `nested_list` takes on the values `[1, 3, 6, 11]`, `[4, 2, 4]`, and `[9, 7, 16, 0]` as the iteration proceeds. We then iterate over the numbers in the current nested list during each iteration. Finally, we print the even numbers.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. Let's try another variation on the even/odd-numbers theme.

We'll return to the simpler one-dimensional version of `my_list`. In this problem, you should write code that creates a new list with one element for each number in `my_list`. If the original number is an even, then the corresponding element in the new list should contain the string `'even'`; otherwise, the element should contain `'odd'`.
    
        my_list = [
        1, 3, 6, 11,
        4, 2, 4, 9,
        17, 16, 0,
    ]
    
    
        # pretty-printed for clarity
    [
        'odd', 'odd', 'even', 'odd',
        'even', 'even', 'even', 'odd',
        'odd', 'even', 'even'
    ]
    

#### Solution
    
        my_list = [
        1, 3, 6, 11,
        4, 2, 4, 9,
        17, 16, 0,
    ]
    
    result = []
    for number in my_list:
        if number % 2 == 0:
            result.append('even')
        else:
            result.append('odd')
    
    print(result)
    

Our approach is straightforward: we iterate over all the numbers in the list and check whether each is even. Based on the result, we append either `'even'` or `'odd'` to the `result` list.

You may have struggled if you tried to use a list comprehension for this problem. Since comprehensions don't have an `else` capability, trying to generate `'even'` for some values and `'odd'` for others is challenging. You can use a ternary expression in the comprehension, but this is a little confusing visually:
    
        my_list = [
        1, 3, 6, 11,
        4, 2, 4, 9,
        17, 16, 0,
    ]
    
    #highlight
    result = [ 'even' if number % 2 == 0 else 'odd'
               for number in my_list ]
    #endhighlight
    print(result)
    

On line 7, we've used a ternary expression to choose between the two values. The ternary is equivalent to:
    
        if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
    

A cleaner approach is to use a helper function to determine whether we should add `'even'` or `'odd'` to the new list:
    
        my_list = [
        1, 3, 6, 11,
        4, 2, 4, 9,
        17, 16, 0,
    ]
    
    #highlight
    def odd_or_even(number):
        return 'even' if number % 2 == 0 else 'odd'
    
    result = [ odd_or_even(number)
    #endhighlight
               for number in my_list ]
    print(result)
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  7. Write a `find_integers` function that returns a list of all the integers from `my_tuple`:
    
        my_tuple = (1, 'a', '1', 3, [7], 3.1415,
                -4, None, {1, 2, 3}, False)
    integers = find_integers(my_tuple)
    print(integers)                    # [1, 3, -4]
    

You can use the expression `type(object) is int` to determine whether an object is an integer. For instance:
    
        print(type(True) is int)      # False (boolean)
    print(type([1, 2, 3]) is int) # False (list)
    print(type(3.141592) is int)  # False (float)
    print(type(77) is int)        # True
    

You may receive a `SyntaxWarning` warning message from the last two examples. You can ignore that warning.

#### Solution
    
        def find_integers(things):
        return [ element
                 for element in things
                 if type(element) is int ]
    
    my_tuple = (1, 'a', '1', 3, [7], 3.1415,
                -4, None, {1, 2, 3}, False)
    integers = find_integers(my_tuple)
    print(integers)                    # [1, 3, -4]
    

Our solution uses a list comprehension to iterate through the elements in the `things` argument and create a new list.

It's worth noting that we used a list comprehension to iterate over the tuple. The main reason for that choice is that `find_integers` is expected to return a list, not a tuple. However, an even more important reason is that there is no such thing as a "tuple comprehension". Comprehensions don't care what kind of collection you're iterating, but the result must always be a list, set, or dictionary.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  8. Write a comprehension that creates a `dict` object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by `my_set` as the source of strings.
    
        my_set = {
        'Fluffy',
        'Butterscotch',
        'Pudding',
        'Cheddar',
        'Cocoa',
    }
    

#### Solution
    
        my_set = {
        'Fluffy',
        'Butterscotch',
        'Pudding',
        'Cheddar',
        'Cocoa',
    }
    
    result = { name: len(name)
               for name in my_set
               if len(name) % 2 != 0 }
    print(result)
    # {'Cheddar': 7, 'Pudding': 7, 'Cocoa': 5}
    

Remember: sets are unordered, so your result may have a different ordering.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  9. Don't let the math scare you. This is a logic and syntax problem, not a math problem.

Write a function that computes and returns the factorial of a number by using a `for` or `while` loop. The factorial of a positive integer `n`, signified by `n!`, is defined as the product of all integers between `1` and `n`, inclusive:

n! | Expansion | Result  
---|---|---  
`1!` | `1` | 1  
`2!` | `1 * 2` | 2  
`3!` | `1 * 2 * 3` | 6  
`4!` | `1 * 2 * 3 * 4` | 24  
`5!` | `1 * 2 * 3 * 4 * 5` | 120  
  
You may assume that the argument is always a positive integer.
    
        print(factorial(1))   # 1
    print(factorial(2))   # 2
    print(factorial(3))   # 6
    print(factorial(4))   # 24
    print(factorial(5))   # 120
    print(factorial(6))   # 720
    print(factorial(7))   # 5040
    print(factorial(8))   # 40320
    print(factorial(25))  # 15511210043330985984000000
    

#### Solution
    
        def factorial(n):
        result = 1
        while n > 0:
            result *= n
            n -= 1
    
        return result
    
    
        def factorial(n):
        result = 1
        for number in range(n, 0, -1):
            result *= number
    
        return result
    

Our first solution uses a `while` loop to compute the return value. We begin by assigning the `result` variable to `1`, then we multiply `result` by all of the integers between `n` and `1`, inclusive. Note that we need to decrement `n` by `1` at the end of each iteration.

The second solution is similar, but it uses a `for` loop instead of a `while` loop. The benefit of using `for` is that we don't need to worry about decrementing `n`. Instead, we just iterate over the integers between `n` and `1`, inclusive, using a range.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  10. The following code uses the `randrange` function from Python's `random` library to obtain and print a random integer within a given range. Using a `while` loop, it keeps running until it finds a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of `randrange`.
    
        import random
    
    highest = 10
    number = random.randrange(highest + 1)
    print(number)
    
    while number != highest:
        number = random.randrange(highest + 1)
        print(number)
    

#### Solution
    
        import random
    
    highest = 10
    while True:
        number = random.randrange(highest + 1)
        print(number)
        if number == highest:
            break
    

The ideal do/while loop use case occurs when you need to execute some code at least once. We need to do that here. However, Python doesn't have a do/while loop. Instead, we can combine a `while True` loop with a `break` statement.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  11. **Challenging Problem** : Don't feel bad if you struggle with this problem or can't solve it. The problem is not easy. It is designed to demonstrate why we prefer to use `for` loops when we can, and a big part of that problem is messy code that is difficult to write and understand. See how far you can get, but don't spend much time struggling.

Print all of the even numbers in the following list of nested lists. This time, don't use any `for` loops.
    
        my_list = [
      [1, 3, 6, 11],
      [4, 2, 4],
      [9, 17, 16, 0],
    ]
    
    
        6
    4
    2
    4
    16
    0
    

#### Solution
    
        my_list = [
      [1, 3, 6, 11],
      [4, 2, 4],
      [9, 17, 16, 0],
    ]
    
    outer_index = 0
    while outer_index < len(my_list):
        inner_index = 0
        while inner_index < len(my_list[outer_index]):
            number = my_list[outer_index][inner_index]
            if number % 2 == 0:
                print(number)
    
            inner_index += 1
    
        outer_index += 1
    

Phew! That's messy and hard to follow, isn't it? While the individual loops aren't tough to understand, keeping track of two different indexes and getting them to work together is no mean feat. We also have to use both indexes on lines 10 and 11.

We can simplify this solution a bit by assigning each nested list to a local variable:
    
        my_list = [
      [1, 3, 6, 11],
      [4, 2, 4],
      [9, 17, 16, 0],
    ]
    
    outer_index = 0
    while outer_index < len(my_list):
        inner_list = my_list[outer_index]
        inner_index = 0
        while inner_index < len(inner_list):
            number = inner_list[inner_index]
            if number % 2 == 0:
                print(number)
    
            inner_index += 1
    
        outer_index += 1
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Variables as Pointers

This chapter examines the concepts behind variables and **pointers**. Specifically, we'll see how Python variables are pointers to a location in memory (an **address space**) that contains the object assigned to the variable. New programmers often struggle to master this concept, but the material is crucial. We'll meet these concepts again in Core.

Developers sometimes talk about **references** instead of pointers. At Launch School, we use these terms interchangeably. You can say that a variable points to or references an object in memory, and you can also say that the pointers stored in variables are references. Some languages make a distinction between references and pointers, but Python does not; feel free to use either term.

## Variables As Pointers

The behaviors described in this chapter arise from the interaction of variables using pointers to reference their associated objects. In Python, all variables are pointers to objects. If you assign the same object to multiple variables, every one of those variables references (points to) the same object. They act like aliases for the object.

When you reassign a variable, Python changes what object the variable references. Reassignment doesn't alter the old or new object; it simply changes which object the variable references.

When a reassignment involves the creation of a new object, Python first creates the new object. It then changes the variable's stack item to point to the new object. As in the previous paragraph, this does not alter the object.

Things get a little messier when mutating objects through a variable. If a variable points to a mutable object and you do something to mutate that object, Python doesn't change the variable; it changes the object. Every variable that references that object will immediately see the object's new state.

The author refers to this as Einsteinian _spooky action at a distance_ or quantum variable entanglement.

The indexing syntax can make things a little confusing. For instance, assume we have a `numbers` list that looks like this:
    
    
    numbers = [1, 2, 3, 4]
    

Now, let's reassign `numbers[2]`:
    
    
    numbers[2] = 3333
    

**This is not a reassignment of the`numbers` variable**. It's a mutation of the list object referenced by `numbers`. Technically, it's also a reassignment of the list object element at index 2, but it is not a mutation of that element.

When using variables, it's essential to remember that some operations mutate objects while others do not. For instance, `list.sort` mutates a list, but `sorted(list)` does not. In particular, you must understand how lines 2 and 3 in the following code differ:
    
    
    x = [1, 2, 3, 4, 5]
    x = [1, 2, 3]
    x[2] = 4
    

Both lines 2 and 3 are reassignments. However, line 3 mutates the list assigned to `x` while line 2 does not mutate anything: it simply reassigns the variable to a new value.

We should also look at augmented assignment. When the variable on the left side references an immutable value, augmented assignment acts like reassignment. Thus, all of the augmented assignments in the following code (lines 6-10) are reassignments since the values referenced on the left are all immutable:
    
    
    a = 42
    b = 3.1415
    c = 'abc'
    d = (1, 2, 3)
    
    a *= 2
    b -= 1
    b /= 3
    c += 'def'
    d += (4, 5)
    

However, if the variable on the left references a mutable value, the augmented assignment is usually mutated. Thus, all the augmented assignments below mutate the value referenced by the variable:
    
    
    a = [1, 2, 3]
    b = {'a', 'b', 'c'}
    
    a += [4, 5]
    a *= 2
    b -= {'b'}
    

All built-in mutable types will be mutated when used as the target of an augmented assignment. However, this behavior is not guaranteed for custom objects, which we'll meet in the Object Oriented Programming book.

The idea that Python stores the elements of a collection in the collection object itself is a simplification of how Python works under the hood. However, it mirrors reality well enough to be a mental model for almost all situations. Don't sweat the details right now; we will expand on this later in the chapter.

It's time to jump into our first real rabbit hole: how variables and objects work in Python.

## Variables and Objects

At the most basic level, variables are named locations in a computer's memory. Each variable has a unique address in memory, usually in an area called the **stack** , and sometimes in a different area called the **heap**. You don't need to understand the differences between the stack and heap at this stage, but learning that they exist will help later in Core.

We'll pretend that all variables are stored on the stack.

The space allocated for a single variable is small. On modern computers in 2023, that's typically 64 bits (or 8 bytes). Objects often far exceed that size. Thus, objects usually aren't stored on the stack. Instead, Python allocates the memory it needs for an object from the heap. Heap blocks can be pretty much any size, provided sufficient memory is available.

Once Python allocates heap space, it creates and stores the object at that location. The address of that object is then copied to the variable's stack location.

Thus, when you access a variable, Python first determines where the variable is on the stack. It then takes the object's heap address from the stack item and uses it to find the object. The variable is a pointer to a stack location, and the stack location is a pointer to the object.

Let's break that down with an example. Assume we're creating a variable named `numbers` and giving it an initial value of a list with 3 numbers:
    
    
    numbers = [1, 2, 3]
    

Since `numbers` is a new variable, Python adds a new entry to the stack. For simplicity, we'll assume the variable's stack address is at memory location 10240.

Next, Python allocates enough memory on the heap to hold the list and its elements (actually, the list object may contain pointers to the elements, but we'll ignore that for now). Let's say that Python allocates 32 bytes at address 4344278784 for the list and its elements. It then constructs an appropriate list object with its elements at address 4344278784.

Finally, Python copies the address 4344278784 into the variable's stack address. Things now look something like this:

![Variable in memory](https://d186loudes4jlv.cloudfront.net/python/images/variable_in_memory.png)

Suppose we now want to print the object assigned to `numbers`:
    
    
    print(numbers)
    

To do this, Python looks up the name `numbers` in its list of variables and sees it is on the stack at address 10240. On the stack, Python can see that the object associated with `numbers` is at address 4344278784. Finally, it passes that address to `print`, which formats and prints the object.

All this sounds incredibly complex for something as conceptually simple as giving a name to some data. Maybe it is. However, in the end, the process is lightning-fast and memory-efficient. There would be almost no benefit to simplifying the process in Python; in fact, it would likely eliminate some crucial benefits.

## Variables and Shared Objects

Let's assign a new variable to the same object that is referenced by `numbers`:
    
    
    numbers2 = numbers
    

Since `numbers2` is new, Python must create a new variable on the stack, which it does. We'll assume it's at address 10256. It then determines the memory address of the object assigned to `numbers` and stores that address in `numbers2`'s stack item. That means both `numbers` and `numbers2` now point to the same object. You can verify this by using the `id` function or the `is` operator:
    
    
    print(id(numbers) == id(numbers2))      # True
    print(numbers is numbers2)              # True
    

Note also that both the `numbers` and `numbers2` ids reference address 4344278784 (or whatever address your Python used for the list):
    
    
    print(id(numbers))            # 4344278784
    print(id(numbers2))           # 4344278784
    

That means our variables and objects are now organized like this in memory:

![Variables sharing an object](//ls-general-public.s3.amazonaws.com/images/python_book/python/images/variables_sharing_an_object-a.png)

The variables are in different places on the stack. However, they both reference the same object.

Pointers have a curious effect when you assign a variable that references an existing object to another variable. Instead of copying the object referenced by the variable on the right to the variable on the left, Python only copies the pointer. Thus, when we initialize `numbers2` with `numbers`, we make both `numbers` and `numbers2` point to the same list object: `[1, 2, 3]`. It's not just the same value but the same list at the same address. The two variables are independent, but since they point to the same list, that list depends on what you do with both `numbers` and `numbers2`.

## Equality and Identity

Two objects, `obj1` and `obj2`, are said to be equal when `obj1 == obj2` returns `True`. The objects are the same object when `obj1 is obj2` returns `True`. We can also say that `obj1` and `obj2` have the same identity since `id(obj1)` and `id(obj2)` return the same value when `obj1 is obj2` returns `True`.

Consider the following code:
    
    
    numbers = [1, 2, 3]
    numbers2 = numbers
    
    print(numbers)                # [1, 2, 3]
    print(numbers == numbers2)    # True
    print(numbers is numbers2)    # True
    
    
    
    numbers = [1, 2, 3]
    numbers2 = [1, 2, 3]
    
    print(numbers)                # [1, 2, 3]
    print(numbers == numbers2)    # True
    print(numbers is numbers2)    # False
    

On line 5 of both examples, `numbers` and `numbers2` are equal since `numbers == numbers2` returns `True`. This makes sense. Both variables point to a list whose values are the same: `1`, `2`, and `3`. As we've already seen, the lists on line 6 of Example 1 are the same objects.

However, are the lists on line 6 of Example 2 the same lists? No, they are not. They are entirely different objects even though they have the same values. As a result, line 6 prints `False`. Line 2 created a new object, which we assigned to `numbers2`. Thus, assuming that the new object is at address 4344281536, memory now looks like this:

![Variables not sharing an object](https://d186loudes4jlv.cloudfront.net/python/images/variables_not_sharing_an_object.png)

## Shallow vs. Deep Copies

When you copy objects in any language, you must understand the difference between shallow and deep copies. Most copies created by Python programs are shallow copies. That might seem strange early on, but it works out for the best. Deep copies just aren't needed all that often. The `copy.copy` and `copy.deepcopy` functions from the built-in `copy` module are Python's primary ways to create shallow and deep copies, respectively.

Before we explore the differences, we must first understand that the memory picture is more complex than we described earlier. Let's take this object as an example:
    
    
    [[1, 2], 3, 4]
    

As we discussed earlier, this object gets created in the heap. However, we assumed that Python would put all 3 elements in the heap memory allocated for the list object. We now have a nested list, though. That list, `[1, 2]`, can't be stored directly in the `[[1, 2], 3, 4]` list. Instead, Python allocates additional memory on the heap for the inner list (`[1, 2]`). Instead of storing `[1, 2]` in the memory allocated for `[[1, 2], 3, 4]`, it stores a pointer to the `[1, 2]` object. Ultimately, the memory picture looks like this:

![Nested lists](https://d186loudes4jlv.cloudfront.net/python/images/nested_lists.png)

As you can see, we have two lists stored at different places in the heap. The outer list on the left contains 3 elements: the integers, `3` and `4`, and a pointer to the second list. The inner list on the right includes integer elements, `1` and `2`.

The actual memory picture is more complicated than this. The integers from both lists are also stored as separate objects. However, we're not interested in them right now, so we won't overcomplicate the diagram.

One last note: the various built-in constructors create shallow copies when passed an element of the same type:
    
    
    my_list = [[1, 2], 3, 4]
    shallow = list(my_list)
    print(shallow[0] is my_list[0])         # True
    
    my_dict = {'abc': [1, 2, 3]}
    shallow = dict(my_dict)
    print(shallow['abc'] is my_dict['abc']) # True
    

The main takeaway is that we have two different objects. Now, let's see what happens when we try to duplicate the first list.

### Shallow Copies

A **shallow copy** of an object is a duplicate of the original object's outermost (topmost) level. Any nested objects within the copied object aren't duplicated; they still reference the nested objects from the original object. Thus, if you mutate the nested objects in the original, those mutations will be visible in the duplicate.

For instance, consider this code:
    
    
    import copy
    
    orig = [[1, 2], 3, 4]
    dup = copy.copy(orig)
    
    print(orig is dup)           # False
    print(orig == dup)           # True
    orig[2] = 44
    print(dup)                   # [[1, 2], 3, 4]
    
    print(orig[0] is dup[0])     # True
    orig[0][1] = 22
    print(dup[0])                # [1, 22]
    

In this example, line 3 creates the list we talked about above. Remember, the list is actually stored as separate objects. Note that `[1, 2]` is referenced by a pointer stored in the original list. We then create a shallow copy of the `orig` list on line 4 and call the duplicate `dup`.

On line 6, we confirm that `orig` and `dup` reference distinct objects. However, line 7 tells us they have the same values. We then mutate `orig` on line 8, then, on line 9, confirm that `dup` hasn't changed. Remember: `orig` and `dup` are separate and distinct objects.

Line 11 shows that both `orig[0]` and `dup[0]` reference the same objects. On line 12, we use `orig[0]` to mutate the `[1, 2]` list. When we print `dup[0]` on line 13, we can see that it reflects the change made to `orig[0]`.

For completeness, here's what memory looks like now. We've reduced the diagram to the bare essentials. We use `[inner]` to represent a pointer to the inner list.

![Shallow copy](https://d186loudes4jlv.cloudfront.net/python/images/shallow_copy.png)

Thus, our shallow copy only duplicated the outermost level of the original list object. The inner list remains shared between the original and duplicate lists.

### Deep Copies

A **deep copy** of an object is an exact duplicate of the original object at the outermost (or topmost) level and every nested object, no matter how deeply nested. There's basically nothing you can do to the original object that can be seen in the duplicate or vice versa.

Let's look at what happens to our previous code example when we introduce deep copies. We've highlighted the differences:
    
    
    import copy
    
    orig = [[1, 2], 3, 4]
    # highlight
    dup = copy.deepcopy(orig)
    # endhighlight
    
    print(orig is dup)           # False
    print(orig == dup)           # True
    orig[2] = 44
    print(dup)                   # [[1, 2], 3, 4]
    
    # highlight
    print(orig[0] is dup[0])     # False
    orig[0][1] = 22
    print(dup[0])                # [1, 2]
    # endhighlight
    

There are no code differences besides using `copy.deepcopy` on line 4. Furthermore, there are no behavioral differences until we reach lines 11-13. Line 11 shows that `orig[0]` and `dup[0]` are no longer the same objects. Thus, when we mutate the `[1, 2]` list referenced by `orig[0]`, we don't see any changes in `dup[0]`.

Note that `copy.deepcopy` doesn't duplicate **everything** ; in most cases, it only duplicates mutable objects. Since immutable objects don't change, there's no need to copy them - references are enough to ensure a deep copy that works.

Here's our final look at the memory picture. We now have two independent "Inner list" objects.

![Deep copy](https://d186loudes4jlv.cloudfront.net/python/images/deep_copy.png)

### Should I Make Deep or Shallow Copies?

The answer to this question depends on your data structure, whether your data structure has mutable content, and whether it matters to your application.

In practice, shallow copies are frequently okay. They work best when:

  * working with objects that are not collections, e.g., integers and booleans. 
  * working with immutable objects with no mutable components, e.g., strings. 
  * working with collections that have no mutable elements, e.g., tuples that don't contain mutable elements. 
  * needed for performance reasons. Shallow copies are always faster. 
  * you don't care if the mutable components of an object are shared. 



You should use deep copies when shallow copies are not okay. In particular, they work best when working with collections that have mutable elements, e.g., nested lists.

## Summary

The takeaway of this chapter is that Python uses pointers to decide which object a variable references. Pointers can lead to surprising and unexpected behavior when two or more variables reference the same object.

##  Exercises

  1. In your own words, explain the difference between these two expressions.
    
        my_object1 == my_object2
    my_object1 is my_object2
    

#### Solution

`my_object1 == my_object2` compares two objects to see whether they are equal. They are considered equal when they have the same value or state. In the case of collections, two collections are equal when they have the same elements.

`my_object1 is my_object2` checks two variables to see whether they reference the same object. An object is the same as another object if both are stored at the same location in memory. In particular, that means we can say that `my_object1` and `my_object2` share the referenced object or that `my_object1` and `my_object2` are aliases for the same object.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  2. Without running this code, what will it print? Why?
    
        set1 = {42, 'Monty Python', ('a', 'b', 'c')}
    set2 = set1
    set1.add(range(5, 10))
    print(set2)
    

Don't worry about having an exact match for the output. The important part is to show something that accurately represents `set2`.

#### Solution

The code outputs:
    
        # The order of the elements probably won't match,
    # but the 4 elements shown here should all be
    # present in your answer.
    
    {('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}
    

This result demonstrates that `set1` and `set2` reference the same set: if we add an element to `set1`, we'll see that element when we look at `set2`. The opposite is true, too: if we add something to `set2`, we'll see it in `set1`.

This code also demonstrates that assigning a variable to another variable doesn't create a new object. Instead, Python copies a reference from the original variable (`set1`) into the target variable (`set2`).

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  3. Without running this code, what will it print? Why?
    
        dict1 = {
        "Hitchhiker's Guide to the Galaxy": 42,
        'Monty Python': 'The Life of Brian',
        'Airplane!': "Don't call me Shirley!",
    }
    
    dict2 = dict(dict1)
    dict2['Monty Python'] = 'Holy Grail'
    print(dict1['Monty Python'])
    

#### Solution

The code outputs:
    
        The Life of Brian
    

The constructor call `dict(dict1)` creates a new dict that contains the same key/value pairs as `dict1`. Thus, `dict2` is not the same object as `dict1`. When we change the value associated with the `'Monty Python'` key in `dict2`, we don't see a corresponding change in `dict1`.

This code demonstrates that two identical objects aren't necessarily the same object. If you assign an object associated with variable `a` to variable `b`, the variables share that object. However, if the value assigned to `b` is an entirely new object, there is no sharing, even if the values are identical.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  4. Without running this code, what will it print? Why?
    
        dict1 = {
        'a': [1, 2, 3],
        'b': (4, 5, 6),
    }
    
    dict2 = dict(dict1)
    dict1['a'][1] = 42
    print(dict2['a'])
    

#### Solution

The code outputs:
    
        [1, 42, 3]
    

As in the previous exercise, the constructor invocation `dict(dict1)` creates a new dict that contains the same key/value pairs as `dict1`. Thus, `dict2` is not the same object as `dict1`.

On line 7, we reassign `dict1['a'][1]` to 42. Since `dict1` and `dict2` are different dicts, you might expect that mutating one of `dict1`'s values would not impact `dict2`. However, that is not the case. The dicts are different objects but share value components since the `dict` constructor creates a shallow copy. Thus, mutations to `dict1['a']` can be seen in `dict2['a']`.

This code demonstrates that two dicts with equal-value objects associated with every key may also share those objects. That isn't always the case, but you must understand what's happening in your code.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  5. Write some code to create a deep copy of the `dict1` object and assign it to `dict2`. You should only modify the code where indicated.
    
        # You may modify this line
    
    dict1 = {
        'a': [[7, 1], ['aa', 'aaa']],
        'b': ([3, 2], ['bb', 'bbb']),
    }
    
    dict2 = ??? # You may modify the `???` part
                # of this line
    
    # All of these should print False
    print(dict1         is dict2)
    print(dict1['a']    is dict2['a'])
    print(dict1['a'][0] is dict2['a'][0])
    print(dict1['a'][1] is dict2['a'][1])
    print(dict1['b']    is dict2['b'])
    print(dict1['b'][0] is dict2['b'][0])
    print(dict1['b'][1] is dict2['b'][1])
    

#### Solution
    
        # highlight
    import copy
    # endhighlight
    
    dict1 = {
        'a': [[7, 1], ['aa', 'aaa']],
        'b': ([3, 2], ['bb', 'bbb']),
    }
    
    # highlight
    dict2 = copy.deepcopy(dict1)
    # endhighlight
    

Deep copies create entirely new objects, including their nested contents. We can use `copy.deepcopy` to create a deep copy.

Note that we don't check the immutable contents of the nested objects inside each list value in the dictionaries. Since they are all immutable, they weren't duplicated. Try it by adding these additional tests.
    
        # All of these should print True
    
    print(dict1['a'][0][0] is dict2['a'][0][0])
    print(dict1['a'][0][1] is dict2['a'][0][1])
    print(dict1['a'][1][0] is dict2['a'][1][0])
    print(dict1['a'][1][1] is dict2['a'][1][1])
    print(dict1['b'][0][0] is dict2['b'][0][0])
    print(dict1['b'][0][1] is dict2['b'][0][1])
    print(dict1['b'][1][0] is dict2['b'][1][0])
    print(dict1['b'][1][1] is dict2['b'][1][1])
    

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

  6. The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of `dict1`. Be careful: **you're not allowed to use the`copy` module in this exercise**.`

In addition, before you run this code, can you predict the output values?
    
        dict1 = {
        'a': [{7, 1}, ['aa', 'aaa']],
        'b': ({3, 2}, ['bb', 'bbb']),
    }
    
    dict2 = ??? # You may modify the `???` part
                # of this line
    
    print(dict1         is dict2)
    print(dict1['a']    is dict2['a'])
    print(dict1['a'][0] is dict2['a'][0])
    print(dict1['a'][1] is dict2['a'][1])
    print(dict1['b']    is dict2['b'])
    print(dict1['b'][0] is dict2['b'][0])
    print(dict1['b'][1] is dict2['b'][1])
    

#### Solution
    
        dict1 = {
        'a': [{7, 1}, ['aa', 'aaa']],
        'b': ({3, 2}, ['bb', 'bbb']),
    }
    
    # highlight
    dict2 = dict(dict1)
    # endhighlight
    
    print(dict1         is dict2)           # False
    print(dict1['a']    is dict2['a'])      # True
    print(dict1['a'][0] is dict2['a'][0])   # True
    print(dict1['a'][1] is dict2['a'][1])   # True
    print(dict1['b']    is dict2['b'])      # True
    print(dict1['b'][0] is dict2['b'][0])   # True
    print(dict1['b'][1] is dict2['b'][1])   # True
    

Since the constructors for Python's built-in collections all return a shallow copy, we used the `dict` constructor to create a shallow copy of `dict1`.

The first `print` statement prints `False` since `dict1` and `dict2` are different objects. However, the nested components are all references to the original nested objects. Thus, the remaining `print` statements print `True`.

**Video Walkthrough**

![Please register to play this video](https://d24f1whwu8r3u4.cloudfront.net/assets/video_placeholders/radial-3c6a470992484f01c619b21118a4cc31e4390ff4a1faf27e7cb792dffa0a57e0.png)

# Additional Python Topics

Let's focus on several useful topics that don't fit elsewhere. Most of these topics aren't crucial for a beginner. However, you will encounter them when you read Python code, documentation, and articles. Be ready!

Some of these topics have enough depth for a separate chapter, if not an entire book! We'll stick to the basics and give you a quick introduction to each.

## Function Composition

A common Python technique is composing function calls, also known as composition. Composition occurs when a function call is used as an argument to another function call, which may, in turn, be passed to another function call. In each case, the return value of the inner function call is used as the argument to the outer function.

### Example
```python
print(list(range(3, 17, 4)))
```
When Python sees code like this, it first evaluates what it can without function calls. In this case, it determines that `3`, `17`, and `4` are integers. It evaluates `range(3, 17, 4)` first, creates the range object, and passes it to `list()`. The final list `[3, 7, 11, 15]` is passed to `print()`.

### Composing Functions
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(num1, num2):
    return num1 * num2

print(times(add(20, 45), subtract(80, 10))) # 4550
```
Here, we pass the return values of `add` and `subtract` to `times`, and then pass the result to `print`. Composition works best when inner functions return useful objects.

## Method Chaining

Well-designed methods tend to do one thing. Method chaining allows calls like this:

### Example
```python
tv_show = "Monty Python's Flying Circus".upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
```
Chaining only works when methods return objects with methods of their own.

### Multi-line Chains
```python
letters = 'abcdefghijklmnoqrstuvwxyz'
consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))
print(consonants)  # bcdfghjklmnqrstvwxyz
```

## Modules

Python allows code reuse through **modules**. These are Python files containing useful functionality.

### Importing Modules
```python
import math
print(math.sqrt(math.pi))  # 1.7724538509055159
```

You can also use `from` for specific imports or aliases:
```python
from math import pi, sqrt
print(sqrt(pi))  # 1.7724538509055159

import math as m
print(m.sqrt(m.pi))  # 1.7724538509055159
```

## Useful Built-in Modules

- **math**: Advanced mathematical operations.
- **datetime**: Date and time manipulation.

### Example: `datetime`
```python
from datetime import datetime as dt
date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)  # Saturday
```

## Function Definition Order

### Example
```python
def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()  # Works because `bottom` is defined before `top` is invoked.
```

## Nested Functions

Functions can be defined inside other functions:

```python
def outer():
    def inner():
        print("Inner function")
    inner()

outer()
```

## `global` and `nonlocal`

These statements let you manage scope explicitly.

### Example: `global`
```python
greeting = 'Hello'

def change_global():
    global greeting
    greeting = 'Hi'

change_global()
print(greeting)  # Hi
```

### Example: `nonlocal`
```python
def outer():
    greeting = 'Hello'

    def inner():
        nonlocal greeting
        greeting = 'Hi'

    inner()
    print(greeting)  # Hi

outer()
```

## Exercises

1. **What does this function do?**
```python
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}
print(do_something(my_dict))
```

2. **Use `math.sqrt` to calculate the square root of 37 in three ways.**

3. **Write a nested function for this code:**
```python
def sum_of_squares(num1, num2):
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))  # 25
```

4. **Fix this bug:**
```python
def all_actions():
    counter = 0

    def increment_counter():
        global counter
        counter += 1

    increment_counter()
    print(counter)

all_actions()
```

---

Experiment with these concepts to deepen your understanding of Python.
