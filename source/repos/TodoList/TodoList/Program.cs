namespace TodoListApp
{
    class Program
    {
        static List<string> todos = new List<string>();

        static void Main(string[] args)
        {
            bool shallExit = false;
            while (!shallExit)
            {
                Console.WriteLine();
                Console.WriteLine("Lets do this thing:");
                Console.WriteLine("[S]ee all TODOs");
                Console.WriteLine("[A]dd a TODO");
                Console.WriteLine("[R]emove a TODO");
                Console.WriteLine("[E]xit");

                var userChoice = Console.ReadLine();

                switch (userChoice)
                {
                    case "s":
                    case "S":
                        SeeAllTodos();
                        break;
                    case "a":
                    case "A":
                        AddTodo();
                        break;
                    case "r":
                    case "R":
                        RemoveTodo();
                        break;
                    case "e":
                    case "E":
                        shallExit = true;
                        break;
                    default:
                        Console.WriteLine("Invalid Choice");
                        break;
                }
            }

            Console.ReadKey();
        }

        static void AddTodo()
        {
            bool isValidDescription = false;
            while (!isValidDescription)
            {
                Console.WriteLine("Enter the TODO description:");
                var description = Console.ReadLine();

                if (description == "")
                {
                    Console.WriteLine("The description cannot be empty");
                }
                else if (todos.Contains(description))
                {
                    Console.WriteLine("The description must be unique.");
                }
                else
                {
                    isValidDescription = true;
                    todos.Add(description);
                }
            }
        }

        static void SeeAllTodos()
        {
            if (todos.Count == 0)
            {
                Console.WriteLine("No TODOs have been added yet.");
            }
            else
            {
                for (int i = 0; i < todos.Count; i++)
                {
                    Console.WriteLine($"{i + 1}. {todos[i]}");
                }
            }
        }

        static void RemoveTodo()
        {
            if (todos.Count == 0)
            {
                Console.WriteLine("No TODOs have been added yet.");
                return;
            }
            bool isIndexValid = false;
            while (!isIndexValid)
            {
                Console.WriteLine("Select the index of the TODO you want to remove:");
                SeeAllTodos();
                var userInput = Console.ReadLine();
                if (userInput == "")
                {
                    Console.WriteLine("Selected index cannot be empty");
                    continue;
                }
                if (int.TryParse(userInput, out int index) &&
                    index >= 1 &&
                    index <= todos.Count)
                {
                    var indexOfTodo = index - 1;
                    var todoToBeRemoved = todos[indexOfTodo];
                    todos.RemoveAt(indexOfTodo);
                    isIndexValid = true;
                    Console.WriteLine("TODO removed: " + todoToBeRemoved);
                }
                else
                {
                    Console.WriteLine("The given index is not valid.");
                }
            }
        }
    }
}