# FOSSite
FOSSite is a project to teach the basics of Linux to spread awareness of the Free and Open Source Software movement.

FOSSite was created with the hope of exposing the general public to the idea of free and open source software. FOSS itself stands for the ideals of software that is accessible to the public and software that allows users to have full control of their software.  We believe that people should not have to restrict their choices to software given in the name of financial gain of the company alone. We believe that instructing the population on FOSS is a moral and social imperative. 

## Runtime: 🇹🇰 ~~http://fossite.tk~~ 🇹🇰  **Server/website has now shut down. Links leading to our site will no longer work. Please read below.** 
## Jekyll README: ~~https://readme.fossite.tk~~ 
### **Server status:**
This repo was made as a project to work on during our 2nd trimester computer science class in 2021-2022. That trimester has ended, and as such, so has the development of this project. Because there is no reason to keep the web server up and running, we have shut it down. Any links leading to our site will no longer work and will timeout. If you want to learn more about free and open source software and Linux, visit: https://itsfoss.com/ or any Linux related sites and/or YouTubers (Like DistroTube, TechHut, Mental Outlaw, etc)

# Table of Contents
- [The People](#the-people)
- [Week 1](#week-1)
- [Week 2](#week-2)

## The People

| Name | Role | Github Profile | Journal | Issues | Scrum Board | Commit History |
| - | - | - | - | - | - | - |
| Sophie Soyeon Park | Scrum Master | [@CalrethilOfMirkwood](https://github.com/CalrethilOfMirkwood) | [Journal](https://docs.google.com/document/d/1pevIAx6l1T2paGKv7fC8DbOfuA8IS8x0SDsPHH6GK3E/edit?usp=sharing) | [Issues](https://github.com/CalrethilOfMirkwood/FOSSite/issues?q=assignee%3ACalrethilOfMirkwood) | [Scrum Board](https://github.com/CalrethilOfMirkwood/FOSSite/projects/1?card_filter_query=assignee%3ACalrethilOfMirkwood) | [Commits](https://github.com/CalrethilOfMirkwood/FOSSite/commits?author=CalrethilOfMirkwood) |
| Krishnadev Lakshminarayanan | Web Designer | [@KrishnadevL](https://github.com/KrishnadevL) | [Journal](https://docs.google.com/document/d/1Yd2N04Y8EEOolwOF8eyXlXfu_NiOpqE99vexkLGeswg/edit?usp=sharing) | [Issues](https://github.com/CalrethilOfMirkwood/FOSSite/issues?q=assignee%3AKrishnadevL) | [Scrum Board](https://github.com/CalrethilOfMirkwood/FOSSite/projects/1?card_filter_query=assignee%3AKrishnadevL) | [Commits](https://github.com/CalrethilOfMirkwood/FOSSite/commits?author=KrishnadevL) |
| Valerie Wilson | GitHub Admin | [@DistilledVinegar](https://github.com/DistilledVinegar) | [Journal](https://docs.google.com/document/d/1XOe0uETl0PM_4bMLgZH6xaBeHtTIXsf2LWUFkF-1XUw/edit) | [Issues](https://github.com/CalrethilOfMirkwood/FOSSite/issues?q=assignee%3ADistilledVinegar) | [Scrum Board](https://github.com/CalrethilOfMirkwood/FOSSite/projects/1?card_filter_query=assignee%3ADistilledVinegar) | [Commits](https://github.com/CalrethilOfMirkwood/FOSSite//commits?author=DistilledVinegar) |https://github.com/CalrethilOfMirkwood/FOSSite/
| Michael Sanborn | Deployment Manager | [@michaelScopic](https://github.com/michaelScopic) | Journal | [Issues](https://github.com/CalrethilOfMirkwood/FOSSite/issues?q=assignee%3AmichaelScopic) | [Scrum Board](https://github.com/CalrethilOfMirkwood/FOSSite/projects/1?card_filter_query=assignee%3AmichaelScopic) | [Commits](https://github.com/CalrethilOfMirkwood/FOSSite/commits?author=michaelScopic) |

# Week 1
Most of week 1 was spent on ideation and planning the course.

| Name | Task |
| - | :--- |
| Sophie | Sophie worked with Valerie to create a rough outline of the [course syllabus](https://docs.google.com/document/d/1Z1GYSwubeXHscKTN5EzRGT2B-IAYzG0vddGxIzL9HNA/edit?skip_itp2_check=true).  She also made her [about page](https://github.com/CalrethilOfMirkwood/FOSSite/issues/2) with a [reddit API](https://github.com/CalrethilOfMirkwood/FOSSite/tree/master/silmarillionmemes.py) (the [error 500 page](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/500.html) links to an alternative page without the API for school wifi). |
| Valreie | Valerie created the syllabus (see above) and also made custom [error pages](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates) and the [about me page](https://github.com/CalrethilOfMirkwood/FOSSite/issues/3).  It has music and other customization. |
| Michael | Michael also worked on the aforementioned syllabus and made his [about page](https://github.com/CalrethilOfMirkwood/FOSSite/issues/1).  He also looked into ideas for deployment, likely on his own server at home. |
| Krish | Krish spent most of his time on wireframing the site, creating a prototype for the [front page](https://github.com/CalrethilOfMirkwood/FOSSite/issues/5#issuecomment-985774706) + [lesson page template](https://github.com/CalrethilOfMirkwood/FOSSite/issues/5#issuecomment-985775037).  To do this he studied bootstrap and CSS. Basic [Directory](https://github.com/CalrethilOfMirkwood/FOSSite/tree/master/templates) was also added to [about me pages](https://github.com/CalrethilOfMirkwood/FOSSite/tree/master/templates/abt_pages) This is planning to be expanded upon by adding seperate python file directory for the about me page and using blueprints. |

# Week 2
Week Summary: Added fully functional about me pages, created navbar to extend across all pages, created base color pallete for website in layout.html, created front landing page 

| Name | Task |
| - | :--- |
| Sophie | Created [image toggle function](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/abt_pages/sophie.html#L18-L31), put it on other team members' pages, and finalized [about page](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/abt_pages/sophie.html). |
| Valreie | Started working on [create task](https://github.com/CalrethilOfMirkwood/FOSSite/issues/13) in pairs with Sophie.  And put [Bible verse API](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/abt_pages/val_about_me.html#L18-L31) on finalized about page. |
| Michael | Started [deployment](https://github.com/CalrethilOfMirkwood/FOSSite/wiki/Deployment) on a personal computer and finalized [about page](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/abt_pages/michaelAbout.html). |
| Krish | Created basic [layout assigned colors](https://github.com/CalrethilOfMirkwood/FOSSite/blob/0716e9eba289887a8b05296f971ef628619c0b3a/templates/layouts/layout.html#L26-L33) based on website theme, Created navbar with [dropdown for webpage](https://github.com/CalrethilOfMirkwood/FOSSite/blob/0716e9eba289887a8b05296f971ef628619c0b3a/templates/layouts/navbar.html#L20-L25), Added old web API to about page and mask [image toggle](https://github.com/CalrethilOfMirkwood/FOSSite/blob/0716e9eba289887a8b05296f971ef628619c0b3a/templates/abt_pages/krish_abt.html#L9-L22). Also changed [image](https://github.com/CalrethilOfMirkwood/FOSSite/blob/0716e9eba289887a8b05296f971ef628619c0b3a/templates/abt_pages/krish_abt.html#L126) on front of about page, created [front page](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/index.html)|

# Week 3
Week Summary: The website now has a semi-functional terminal emulator and a sample lesson page.  There file system has been completely reorganized.

Week Review Video: https://drive.google.com/file/d/13PMKKLhJQSZeFc7bavTpaQyBmh2xBkOD/view
| Name | Task |
| - | :--- |
| Sophie | Created [terminal emulator](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/terminal.html) and helped Krish with the reorganizing. |
| Valreie | Worked on the [terminal emulator](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/terminal.html) with Sophie. |
| Michael | Worked on [deployment](https://github.com/CalrethilOfMirkwood/FOSSite/wiki/Deployment). |
| Krish | Created [site-wide layout](https://github.com/CalrethilOfMirkwood/FOSSite/blob/master/templates/layouts/layout.html) and completely reorganized website [file layout](https://github.com/CalrethilOfMirkwood/FOSSite/commit/c02599d588552ced02636a6a00bc4d9daa5d9a3d).|

# Week 7
Week Summary: FOSSchan (with a customized theme) and snake are now deployed on the website.  There is an updated, more comprehensive dark mode.  FOSSweaper is in development.

| Name | Task |
| - | :--- |
| Sophie | Created [FOSSchan](https://github.com/CalrethilOfMirkwood/FOSSite/tree/master/database), a pseudo-forum based on SQLite similar the app Whisper where people can post anonymously.  Also helped Valerie with [snake](https://github.com/CalrethilOfMirkwood/FOSSite/commit/dcc4cf50981ef635a45e39c2a9ffbfd89c0b515e) and trying to convert it into minesweeper. |
| Valreie | Deployed [snake](https://github.com/CalrethilOfMirkwood/FOSSite/commit/dcc4cf50981ef635a45e39c2a9ffbfd89c0b515e) on the website.  Currently trying to turn it into a minesweeper game.  Making a python mock-up with the intent to convert it into javascript for an html page. |
| Michael | Worked on [deployment](https://github.com/CalrethilOfMirkwood/FOSSite/wiki/Deployment). |
| Krish | Created [custom design for FOSSChan](https://github.com/CalrethilOfMirkwood/FOSSite/commit/f39d98a89910b247c42d52a415c9de42dd2f61ff) and revamped the [dark mode](https://github.com/CalrethilOfMirkwood/FOSSite/commit/f39d98a89910b247c42d52a415c9de42dd2f61ff).  FOSSchan's boxes are now properly sized and the dark mode actually darkens the webpage with aesthetically pleasing colors. |

# Week 8
Week Summary: Crossover coding, got CRUD+asynchronous database deployed and how succesful it was is debatable.

| Name | Task |
| - | :--- |
| Rebecca | Got the CRUD+asynchronous database deployed. | <!-- The database is not real.  It never existed. -->
| Gabriel | Created the searchbar. It searches through through a page index with linear search. | <!-- Never committed... -->
| Tianbin | Got the quiz going, it is multiple choice+score tracking+randomizing with an aesthetic video background. | <!-- genshin impact -->
| Sophie | Tried to get the terminal actually functional. Wasn't able to do that but wrote the questions for the quiz. | <!-- My ego is too fat for this. -->
