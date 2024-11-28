using System.Timers;
using System.Diagnostics;
using System.Collections.ObjectModel;

namespace Pomodoro
{
    public partial class MainPage : ContentPage
    {
        private PomodoroTimer _pomodoroTimer;
        private TimerOptions _timerOptions;
        private TodoManager _todoManager;
        private System.Timers.Timer _uiTimer;

        public MainPage()
        {
            InitializeComponent();
            NavigationPage.SetHasNavigationBar(this, false); // Remove the navigation bar
            _pomodoroTimer = new PomodoroTimer(25 * 60000, 5 * 60000);
            _timerOptions = new TimerOptions(_pomodoroTimer);
            _todoManager = new TodoManager();
            _uiTimer = new System.Timers.Timer(1000);
            _uiTimer.Elapsed += UpdateTimerLabel;

            TodoListView.ItemsSource = _todoManager.GetAllTodos();
        }

        private void UpdateTimerLabel(object? sender, ElapsedEventArgs e)
        {
            Dispatcher.Dispatch(() =>
            {
                TimerLabel.Text = _pomodoroTimer.GetTimeLeft().ToString(@"hh\:mm\:ss");
            });
        }

        private void OnStartTimerClicked(object sender, EventArgs e)
        {
            _timerOptions.StartTimer();
            _uiTimer.Start();
        }

        private void OnPauseTimerClicked(object sender, EventArgs e)
        {
            _timerOptions.PauseTimer();
            _uiTimer.Stop();
        }

        private void OnCancelTimerClicked(object sender, EventArgs e)
        {
            _timerOptions.CancelTimer();
            _uiTimer.Stop();
            TimerLabel.Text = "00:00:00";
        }

        private async void OnSeeAllTodosClicked(object sender, EventArgs e)
        {
            var todos = _todoManager.GetAllTodos();
            if (todos.Count == 0)
            {
                await DisplayAlert("TODOs", "No TODOs have been added yet.", "OK");
            }
            else
            {
                var todoListWithIndices = new ObservableCollection<string>();
                for (int i = 0; i < todos.Count; i++)
                {
                    todoListWithIndices.Add($"{i + 1}. {todos[i]}");
                }

                string todoList = string.Join("\n", todoListWithIndices);
                await DisplayAlert("TODOs", todoList, "OK");
            }
        }

        private async void OnAddTodoClicked(object sender, EventArgs e)
        {
            string description = await DisplayPromptAsync("New TODO", "Enter the TODO description:");
            if (!string.IsNullOrEmpty(description))
            {
                try
                {
                    _todoManager.AddTodo(description);
                    OnSeeAllTodosClicked(sender, e);
                }
                catch (ArgumentException ex)
                {
                    await DisplayAlert("Error", ex.Message, "OK");
                }
            }
        }

        private async void OnRemoveTodoClicked(object sender, EventArgs e)
        {
            string indexStr = await DisplayPromptAsync("Remove TODO", "Enter the number of the TODO to remove:");
            if (int.TryParse(indexStr, out int index))
            {
                try
                {
                    Debug.WriteLine($"select the number you want to remove: {index - 1}");
                    _todoManager.RemoveTodoAt(index - 1);
                    Debug.WriteLine("TODO removed successfully");
                    OnSeeAllTodosClicked(sender, e);
                }
                catch (ArgumentOutOfRangeException ex)
                {
                    await DisplayAlert("Error", ex.Message, "OK");
                }
            }
            else
            {
                await DisplayAlert("Error", "Invalid index", "OK");
            }
        }

        private async void OnSelectRandomTodoClicked(object sender, EventArgs e)
        {
            var todos = _todoManager.GetAllTodos();
            if (todos.Count == 0)
            {
                await DisplayAlert("TODOs", "No TODOs have been added yet.", "OK");
            }
            else
            {
                Random random = new Random();
                int randomIndex = random.Next(todos.Count);
                string selectedTodo = todos[randomIndex];
                await DisplayAlert("Start Working", $"Start working on: {selectedTodo}", "OK");
            }
        }
    }
}
