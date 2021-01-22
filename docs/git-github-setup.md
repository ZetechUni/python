# GitHub Setup

> GitHub offers the distributed version control and source code management and collaboration.

**Below are resources to getting started with GitHub.**

> You are supposed to complete the practical activities after going through the resources for you to qualify to the next stage.

| Be sure to have the basic knowledge of using github: |
|--|
| Creating a repository |
| Forking a repository |
| Updating a Forked Repository |
| Creating a Branch |
| Creating a Pull Request |
| Creating a Issues |

## GitHub Basics

1. [Official Guides by GitHub](https://guides.github.com/)
2. [Creating a Repository](https://guides.github.com/activities/hello-world/)
3. [Getting Started With GitHub](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github)

## Git Setup

What is git?
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Resources:

[git-scm website](https://git-scm.com/)
[Downloading git](https://git-scm.com/download)
[Configuring git with GitHub](https://chrisdev.hashnode.dev/git-and-github-installation-and-configuration)

## Practical Activities

### Activity 1:

- Create a GitHub Repository using your account.
- Use your GitHub username as the name of the repository, (Exact characters)
- Clone the repository to your local environment, using either git or gh-cli.
- Create a new file: 
  
  >Use the following naming convection: {github-username}.txt
- Add the following details to the created file: 

    >your github username and your github email

- Update your repository using `git`. 
    
    i.e: 

    ```shell
    git add .
    git commit -m "your commit message"
    git push
    ```

    N.B Use a better commit message.

### Activity 2

- Head over to https://github.com/ZetechUni/github-collaborations
- Fork the repository
- Create a new branch using the following naming convection: ({github-username}-patch)
- Add the following details in the README.md under the "Contributors" title:
- Your GitHub Username
    - The Link to Repository Created in Activity 1
    - A sentence describing who you are:
    - The Format will be as follows:

    ```markdown
    |#    |    {user-name}     |     {repo-link}    |    {about-me}     |
    ```
- Update your repository.
- Create a pull request.
- After creating a pull request, create an issue using the same name as the pull request: