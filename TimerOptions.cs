namespace Pomodoro
{
    public class TimerOptions
    {
        private PomodoroTimer _pomodoroTimer;

        public TimerOptions(PomodoroTimer pomodoroTimer)
        {
            _pomodoroTimer = pomodoroTimer;
        }

        public void StartTimer()
        {
            _pomodoroTimer.Start();
        }

        public void PauseTimer()
        {
            _pomodoroTimer.Pause();
        }

        public void ResumeTimer()
        {
            _pomodoroTimer.Resume();
        }

        public void CancelTimer()
        {
            _pomodoroTimer.Cancel();
        }

        public void ShowTimeLeft()
        {
            _pomodoroTimer.ShowTimeLeft();
        }
    }
}
