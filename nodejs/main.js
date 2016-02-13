var Task=require('./task3');


var task1=new Task('create a demo for constructor');
var task2=new Task('create a demo for module');
var task3=new Task('create a demo for singletons');
var task4=new Task('create a demo for prototype');

task1.complete();
task2.save();
task3.save();
task4.save();