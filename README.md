## DNA PROJECT
### Description
This project stands for creating and manipulating DNA sequences,
using special commands.

### Classes
The project is consists of the following classes:
* data_base:
    * DnaSequence: represents a single dna sequence - holds a string of nucleotides.
    * Sequence: represents a single sequence with an information about it - holds sequence id, name, status and dna sequence.
    * DnaCollectionManager: represents a sequences collection and manages it with special methods.
    * BatchCollectionManager: represents a batches collection and manages it with special methods.


* command:
    * Command: represents a generic command.
    * CommandsFactory: holds all the allowed commands and can translate a command string to command object.
    * CommandsInvoker: manages the commands running - can run a specific command.
    * commands: a class for each allowed command which manages the flow of this command.
    

* terminal:
    * Cli: represent a generic cli - terminal for communication with the user.
    * Cmd: represents the main cli.
    * Confirm: represents a confirm mode of the cli.
    * Batch: represents a batch mode of the cli.

### Design
In this project I used three design patterns:
* ** Singleton**:
    _Restricts object creation for a class to only one instance._
  
    I used this pattern to restrict the databases to be single.
* ** Command**:
    _Creates objects that encapsulate actions and parameters._
  
    I used this pattern for manage the different commands.
* ** Factory**:
    _Creates objects without specifying the exact class to create._
  
    I used this pattern to create the commands objects.
