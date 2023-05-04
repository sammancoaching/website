---
title: Audit everything
kata_name: audit
---

## Audit everything
The `Audit` project is an audit system that keeps track of all visitors in an organization.
It : 
* uses flat text files as underlying storage with the structure shown below
* system appends the visitor’s name and the time of their visit to the end of the most recent file
    - When the maximum number of entries per file is reached: a new file with an `incremented index` is created

![Audit file example](/assets/images/audit-example.png)

### The system
```c#
namespace Audit
{
    public class AuditManager
    {
        private readonly int _maxEntriesPerFile;
        private readonly string _directoryName;
        private readonly IFileSystem _fileSystem;

        public AuditManager(
            int maxEntriesPerFile, 
            string directoryName,
            IFileSystem fileSystem)
        {
            _maxEntriesPerFile = maxEntriesPerFile;
            _directoryName = directoryName;
            _fileSystem = fileSystem;
        }
    
        public void AddRecord(string visitorName, DateTime timeOfVisit)
        {
            string[] filePaths = _fileSystem.GetFiles(_directoryName);
            (int index, string path)[] sorted = SortByIndex(filePaths);
            var newRecord = visitorName + ';' + timeOfVisit.ToString("yyyy-MM-dd HH:mm:ss");
        
            if (sorted.Length == 0)
            {
                string newFile = Path.Combine(_directoryName, "audit_1.txt");
                _fileSystem.WriteAllText(newFile, newRecord);
            
                return;
            }
        
            (int currentFileIndex, string currentFilePath) = sorted.Last();
            List<string> lines = _fileSystem.ReadAllLines(currentFilePath).ToList();
        
            if (lines.Count < _maxEntriesPerFile)
            {
                lines.Add(newRecord);
                string newContent = string.Join(Environment.NewLine, lines);
                _fileSystem.WriteAllText(currentFilePath, newContent);
            }
            else
            {
                int newIndex = currentFileIndex + 1;
                string newName = $"audit_{newIndex}.txt";
                string newFile = Path.Combine(_directoryName, newName);
                _fileSystem.WriteAllText(newFile, newRecord);
            }
        }

        private static (int index, string path)[] SortByIndex(string[] filePaths)
            => filePaths
                .AsEnumerable()
                .Select((path, index) => (index + 1, path))
                .ToArray();
    }
}
```

AuditManager is the main class in the application. 
Its constructor accepts the maximum number of entries per file and the working directory as configuration parameters. 

The only public method in the class is `AddRecord`, which does all the work of the audit system:
* Retrieves a full list of files from the working directory
* Sorts them by index (all filenames follow the same pattern: `audit_{index}.txt` [for example, audit_1.txt])
* If there are no audit files yet, creates a first one with a single record
* If there are audit files, gets the most recent one and either appends the new record to it or creates a new file, depending on whether the number of entries in that file has reached the limit

## Acknowledgement
This kata has been described by [Vladimir Khorikov](https://www.linkedin.com/in/vladimir-khorikov-bb482653/) in his great book [Unit Testing Principles, Practices, and Patterns](https://www.manning.com/books/unit-testing).