/*
* valentine.js
*/

/*
* your csrf-token
*/
var csrf = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';

/*
* brute-force-method for finding search keywords
*/
var searchterms = [];

var alphabets = "abcdefghijklmnopqrstuvwxyz".split('');

for(var i=0;i<26;i++)
{
   for(var j=0;j<26;j++)
   {
       for(var k=0;k<26;k++)
       {
            searchterms.push(alphabets[i]+alphabets[j]+alphabets[k]);
       }
   }
}

/*
* worker characteristics : id, search-keyword-range(start,end)
*/
function workers(a,b,c){
    this.id = a;
    this.start = b;
    this.end = c;
}

/*
* sendrose function : sends roses to every result(person) of search-keywords in its respective range
*/
workers.prototype.sendrose = function(){
    var id = this.id;
    for(var i=this.start;i<=this.end;i++)
    {
        $.get('https://channeli.in/connect-e-dil/person_search/?term='+searchterms[i],function(data){
            var len = data.length;
            for(var l=0;l<len;l++)
            {
                var human = data[l];
                var msg = 'this red rose is sent to you by worker '+id+ '#HappyValentineDay...he made sure that he wishes to everyone here';
                $.post('https://channeli.in/connect-e-dil/',{csrfmiddlewaretoken:csrf,person:human.value,enroll:human.id,rose_colour:'YR',message:msg,rossy: 'Send'});
                console.log('worker '+id+' is sending message to '+human.value);
            }
        });
    }
}

// using workers to make script faster then linear
var worker = new Array(104);

// total brute-forced keywords
var total = searchterms.length; // 17576 = 104*169

// assigning ranges(in search-keywords) for each workers
for(var i=0;i<104;i++)
{
    worker[i] = new workers(i+1,i*169,(((i+1)*169)-1));
}

// activating each workers
for(var i=0;i<worker.length;i++)
{
    worker[i].sendrose();
}