# Project Manager

FastAPI-based project management application.

                                            Multi-Service Task Management Application 
This application is much like a simple To Do list managing application.Here user first register in the system or log . then create a project and create sub tasks there . then he can give priority to subtasks and he can search sub tasks by name or priority . User can select the project status there (begun , on going , finished) .Application has feature for export reports generated according to users productivity and other measurable statistics . 

Core Functionalities :

    Authentication & users 
        Endpoints :-  
            Login / Register
            Token validation

    Project & Task Management 
        Endpoints :- 
            Create / update / delete tasks
            Bulk task creation
            Filter + search tasks

    Search & Filtering Engine
        Endpoint :- 
            Search tasks by text
            Filter by status, date, user
            Sort by priority

    Reporting & Aggregation
        Endpoint :- 
            Tasks completed per day
            Average task completion time
            User productivity metrics 

    Background Jobs
        Endpoints :-  
            Daily report generation
            Old data cleanup
            Activity log summarization

    File / Payload Handling 
        Endpoints :- 
            Upload attachments to tasks
            Download task exports
