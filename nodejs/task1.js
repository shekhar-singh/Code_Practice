//var tast={};

var task = {
	title :'my task',
    discription:'My discription'
};

Object.defineProperty(task,'toString',{
	value:function(){
		return this.title +' '+this.discription;
	},
	writable:false, //unbreakble u cant overwrite functns
	enumerable:false, //dont show iter function { title: 'my task',discription: 'My discription',toString: [Function] }

	configurable:false//u cant redefine and change value
});

//console.log(task.toString());
console.log(task);