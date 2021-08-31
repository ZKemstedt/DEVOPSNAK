# Thursday March 11th

## Content
* PATH
* Argument
* input, output, redirection
* Fore- and Background processes
* jobcontrol
* exit codes
* Signals ()
TLCL chapters 6, 7, 10

## Terminology
stdin, stdout, stderr
'pipe to'
```sh
&           backgroun job
&&          if successfull, then...
|           forward 'pipe'
||          if error, then ...
<           write to
>           write to
<<          append
>>          append
```

--- 

# Processes
1. Fork
2. Exec

Sometimes the shell create subshells for certain tasks
`$ ps -ef | grep $USER | tail`
`$ (ps -ef | grep $USER) | tail`

Each Terminal can have at most 1 foreground process
To start a process in the background:
`$ free -s 4 &`
To bring a background process into the foreground:
`$ fg %1` where the number after % is the job id
`$ fg 1` also works, usually
`$ fg` is equivalent to `$ fg %1`

ctrl-Z will send a process to the background, but it will be paused. use bg or fg to start it
```sh
fg
bg
jobs
```

Stopping a process
[ctrl-Z] only works for foreground processes.
`$ kill 1234` stops the process with PID 1234.
`$kill %s` stops the process with jobb-id 2.

You can only kill your own processes unless you're root

kill sends a signal to the process, default is SIGTERM (15)

top
htop

signaler

## Filter
...



gist.github.com/311377