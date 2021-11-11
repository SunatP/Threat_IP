# FortiSIEM's Threat IP and other IOC sources

## Why should we do this one?

From the past, we run the code files and, it will export the CSV file manually by my hand. Sometimes we forget to execute the code cause we have another task to do every day. That's why these code files become to this repository.

## What do these code files can do?

By default, all of these files generate the dataset for FortiSIEM. These code files are based on the Jupyter Notebook environment which, is basically from the python language by default. Following the previous one, since we have many tasks in daily life (every day). Moreover, sometimes we forget to run the code by hand, that's means we didn't have CSV file(s) imported to FortiSIEM on that day(s). We decided to create these files from scratch from our environment (personal laptop) and fix many bugs in the line of code that errors while executing. Also, we adapted code based on Jupyter Notebook into purely python-based 100%. Furthermore, we applied all of the code files to the Jenkins CI/CD. So, we don't need to run these codes with our hands anymore and, they should run by automatically since we set them periodically (every day at noon).

## Why do we use Jenkins CI/CD, not crontab?

We use Jenkins because it gives all visibility tasks, config options when we compare with the contrab. We can also farm out the workload using a CI build server that we have already depended on day by day.

## What do we need to implement this one?
- Minimum hardware requirements: 256 MB of RAM. 1 GB of drive space (although 10 GB is a recommended minimum if running Jenkins as a Docker container)
- High-speed internet
- Python3
    - pip3 library
    - pandas library
- Text Editor (Notepad++, Visual Studio Code, Vim, Nano, etc.)
- Jenkins