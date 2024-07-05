## Setup
Navigate to the folder containing ***requirements.txt*** in it: `cd ToDoApp`.
- In terminal type `pip install -r requirements.txt`
- This will install all the required dependencies for the project.

## Development
Run the project with `uvicorn main:app --reload`
- If `todosapp.db` doesn't exists, it'll be created.

The project should now be available at: http://127.0.0.1:8000/
- It will by default return all the ToDo items
- To use Swagger documentation instead, hit http://127.0.0.1:8000/docs

### Testing data
To try out the endpoints that need authorization you can use the following:
 - `freddydev` / `password`
 - `test` / `1234`

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
