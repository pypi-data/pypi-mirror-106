# RandomTables

little module that helps to create tables for a specified schema with random content

### How to use
To create a random table you can specify a schema upfront and then call the class

```
from randomtables import DataSetGenerator

# define schema
schema = [
    {"type": float}, 
    {"type": int},
    {"type": str, "split": False},
    {"type": str, "split": True, "names": True}
]

# initialize the schema
dfg = DataSetGenerator()

# generate a pandas dataframe
data = dfg.generate(
    schema = schema,
)

```
