# General Info
This a To-do app done in Python using FastAPI. 
It provides:
- User authentication and registration.
- A CRUD for the user's todos.
- Ability to mark a todo as complete.
- Swagger documentation for every endpoint implemented.
- Unit testing via `pytest` for endpoint coverage. 

### Live Demo
https://python-todoapp-deployment.onrender.com/

## Setup
Navigate to the folder containing ***requirements.txt*** in it: `cd ToDoApp`.
- In terminal type `pip install -r requirements.txt`
- This will install all the required dependencies for the project.

## Development
Run the project with `uvicorn ToDoApp.main:app --reload`
- If `todosapp.db` doesn't exists, it'll be created.

The project should now be available at: http://127.0.0.1:8000/
- It should load the login screen, use the testing data to log in or register as new user.
- To use Swagger documentation instead, hit http://127.0.0.1:8000/docs

### Testing data

#### Manual testing
To try out the endpoints that need authorization you can use the following:
 - `freddydev` / `password`
 - `test` / `1234`

#### Unit testing
Run `pytest --disable-warnings` to trigger the project validations
 - the flag `--disable-warnings` is added to prevent warnings from lib dependencies

## SQL Queries
Open `todosapp.db` with `sqlite3`. This allows us to execute SQL queries in the terminal.
```bash
 sqlite3 todosapp.db
```

`insert` and `select` data

```bash
❯ sqlite3 todosapp.db
sqlite> select * from todos;
sqlite> insert into todos (title, description, priority, complete) values ('Go to the store', 'Buy eggs', 5, False);
sqlite> insert into todos (title, description, priority, complete) values ('Do homework', 'Math exercises', 2, False);
sqlite> insert into todos (title, description, priority, complete) values ('Feed the dog', 'Get a bone', 3, False);

sqlite> select * from todos;
1|Go to the store|Buy eggs|5|0
2|Do homework|Math exercises|2|0
3|Feed the dog|Get a bone|3|0

sqlite> .mode column
sqlite> select * from todos;
id  title            description     priority  complete
--  ---------------  --------------  --------  --------
1   Go to the store  Buy eggs        5         0       
2   Do homework      Math exercises  2         0       
3   Feed the dog     Get a bone      3         0       

sqlite> .mode markdown
sqlite> select * from todos;
| id |      title      |  description   | priority | complete |
|----|-----------------|----------------|----------|----------|
| 1  | Go to the store | Buy eggs       | 5        | 0        |
| 2  | Do homework     | Math exercises | 2        | 0        |
| 3  | Feed the dog    | Get a bone     | 3        | 0        |

sqlite> .mode box
sqlite> select * from todos;
┌────┬─────────────────┬────────────────┬──────────┬──────────┐
│ id │      title      │  description   │ priority │ complete │
├────┼─────────────────┼────────────────┼──────────┼──────────┤
│ 1  │ Go to the store │ Buy eggs       │ 5        │ 0        │
│ 2  │ Do homework     │ Math exercises │ 2        │ 0        │
│ 3  │ Feed the dog    │ Get a bone     │ 3        │ 0        │
└────┴─────────────────┴────────────────┴──────────┴──────────┘
```
