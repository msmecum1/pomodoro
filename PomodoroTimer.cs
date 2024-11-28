using System.Timers;

namespace Pomodoro
{
    public class PomodoroTimer
    {
        private System.Timers.Timer _timer;
        private int _workDuration;
        private int _breakDuration;
        private bool _isWorkTime;
        private DateTime _endTime;
        private TimeSpan _remainingTime;

        public PomodoroTimer(int workDuration, int breakDuration)
        {
            _workDuration = workDuration;
            _breakDuration = breakDuration;
            _isWorkTime = true;
            _timer = new System.Timers.Timer();
            _timer.Elapsed += OnTimedEvent;
        }

        public void Start()
        {
            SetTimer(_workDuration);
        }

        public void Pause()
        {
            _timer.Stop();
            _remainingTime = _endTime - DateTime.Now;
        }

        public void Resume()
        {
            SetTimer((int)_remainingTime.TotalMilliseconds);
        }

        public void Cancel()
        {
            _timer.Stop();
            _remainingTime = TimeSpan.Zero;
        }

        public void ShowTimeLeft()
        {
            Console.WriteLine(GetTimeLeft().ToString(@"hh\:mm\:ss"));
        }

        public TimeSpan GetTimeLeft()
        {
            return _endTime - DateTime.Now;
        }

        private void SetTimer(int duration)
        {
            _endTime = DateTime.Now.AddMilliseconds(duration);
            _timer.Interval = duration;
            _timer.Start();
        }

        private void OnTimedEvent(object? source, ElapsedEventArgs e)
        {
            _timer.Stop();
            _isWorkTime = !_isWorkTime;
            SetTimer(_isWorkTime ? _workDuration : _breakDuration);
        }
    }
}