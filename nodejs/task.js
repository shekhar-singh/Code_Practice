//var tast={};

var task=Object.create(Object.prototype);
task.title='my task';
task.discription='My discription';
task.toString=function(){
	return this.title +' '+this.discription;
}
console.log(task.toString());