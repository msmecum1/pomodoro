using System.Collections.ObjectModel;
using System.Diagnostics; 

public class TodoManager
{
    private ObservableCollection<string> todos = new ObservableCollection<string>();

    public void AddTodo(string description)
    {
        if (string.IsNullOrEmpty(description))
        {
            throw new ArgumentException("The description cannot be empty");
        }
        if (todos.Contains(description))
        {
            throw new ArgumentException("The description must be unique.");
        }
        todos.Add(description);
    }

    public ObservableCollection<string> GetAllTodos()
    {
        return todos;
    }

    public void RemoveTodoAt(int index)
    {
        if (index < 0 || index >= todos.Count)
        {
            throw new ArgumentOutOfRangeException(nameof(index), "The given index is not valid.");
        }
        Debug.WriteLine($"Removing TODO at index: {index}");
        todos.RemoveAt(index);
        Debug.WriteLine("TODO removed from list");
    }
}
