let k = 0, a= 0;
let s = "";
let srtkiva = "Smetanka"
let allsb =""
let adstr = ""
unicname = []
const myperson = 
    {
      name: "Артем",
      surname: "Абрашин",
      d:01,
      m:03,
      y:2003
    }
  const sisters = [
    "Wiolet 2003",
    'Anna 2000',
    'Lisa 2001',
    'Masha 2003',
    'Ira 2004',
    'Sveta 2009',
    'Anna 2003'
  ]
  let masssort = [[]]
  let sortar = []
  let strt = ''
  let mass = [[ ]]
  let iters = []

  for (let i = 0; i < sisters.length; i++)
    {
      strt = sisters[i]
      mass[[i]] = strt.split(' ')
      mass[[i]].reverse()
    }

  for (let i = 0; i < mass.length; i++)
    {
      sortar[i] = mass[i][0]
    }

   for (let i = 0; i < mass.length; i++)
    {
      let lower = 0
      for (let j = 0; j < mass.length; j++)
      {
        if (sortar[j] < sortar[lower])
        lower = j;
      }

    iters[i] = lower;
    sortar[lower] = 10000

   }
   


  for (let i = 0; i < sisters.length; i++)
  {
     strt = sisters[i]
   masssort[[i]] = strt.split(' ')
   
 }

function sortir(){
  masssort.sort()
  masssort.reverse()
  obj2.innerHTML = " Список родственников(сестер): "
  obj2.innerHTML += "<br>"
  for (let pa of masssort) {
  
    obj2.innerHTML += "<br>"
    obj2.innerHTML += pa[0]
    obj2.innerHTML += "     "
    obj2.innerHTML += " : "
    obj2.innerHTML += pa[1]  
}
}

timer = setInterval(function () {

    let now = new Date();
    let date = new Date(2024, 03, 02);
    end = date - now;

    if (end <= 0) {
    
        clearInterval(timer);
        alert("time to celebrate");
    } else {
        let res = new Date(end);
        let seconds = `${res.getUTCSeconds()}`
        let   minutes = `${res.getUTCMinutes()}`;
        let hours = `${res.getUTCHours()}`
        let day = `${res.getUTCDate() - 1}`
        let mounth = `${res.getUTCMonth() -1 }`
        let year =  `${res.getUTCFullYear() - 1970 }`

        if ( `${date.getUTCMonth()  }` !=`${now.getUTCMonth() +1  }`)
        day = `${ res.getUTCDate() + 2}`

        else 
       day = `${ res.getUTCDate() - 1}`

        if ( seconds < 10)
        
         seconds = `0${res.getUTCSeconds()}`
        

         if ( minutes < 10)
         minutes = `0${res.getUTCMinutes()}`
         
         if (hours < 10)
        hours = `0${res.getUTCHours()}`

        if ( `${date.getUTCMonth() }` != `${now.getUTCMonth()  +1 }` && day < 10)
         day = `0${ res.getUTCDate() -1 }`
        else if ( day < 10)
        day = `0${ res.getUTCDate() - 1}`
        if ( `${date.getUTCMonth()  }` != `${now.getUTCMonth() +1 }`)
        {
          mounth = `${res.getUTCMonth() -1 }`
          if (mounth < 10)
         mounth = `0${res.getUTCMonth() -1 }`
        }
        else if (mounth < 10)
         mounth = `0${res.getUTCMonth() -1 }`
         if (year < 10)
         year = `0${res.getUTCFullYear() -1970  }`
       if ( date.getFullYear() - now.getFullYear() != 0)
        if(date.getMonth() == now.getMonth()+1)
         {
          if (date.getDate() - now.getDate() > 0 ) {
          year = `0${res.getFullYear() - 1970}`
          mounth = `0`
          day = date.getDate() - now.getDate() - 1
          } else  if (date.getDate() - now.getDate() < 0 ) {
            year = `0`
            mounth = `11`
            day = 28 - (now.getDate()- date.getDate()) + now.getDate() - 1
            }
         }
 
    
        document.getElementById("sec").innerHTML=seconds;
        document.getElementById("min").innerHTML=minutes;
        document.getElementById("hou").innerHTML=hours;
        document.getElementById("day").innerHTML=day;
        document.getElementById("mou").innerHTML=mounth;
        document.getElementById("year").innerHTML=year;
    }
}, 1000)

const arr = new Map([

    [ 'алгебра', '5'],
    [ 'физика', '4'],
    [ 'русский', '4'],
    ['география', '5'],
    [ 'биология', '4'],
    [ 'химия', '4'],
    [ 'физра', '5'],
    [ 'геометрия', '4'],
    [ 'история', '4'],
    [ 'литература', '5'],
    [ 'английский', '4'],
    [ 'лабы', '4']
]);

let obj = document.getElementById('obj');
let obj2 = document.getElementById('obj2')
let obj3 = document.getElementById('obj3')
let obj4 = document.getElementById('obj4')
let obj5 = document.getElementById('obj5')
let kiva = document.getElementById('Kiva');

for (let pair of arr) {
    
obj.innerHTML += "<br>"
obj.innerHTML += ` ${pair[0]}`
obj.innerHTML += ": "
obj.innerHTML += "  "
obj.innerHTML += +  `${pair[1]}`    
k = Number(pair[1]);
s +=pair[0]
a = a + k;
  }

for (let pa of masssort) {
    
    obj2.innerHTML += "<br>"
    obj2.innerHTML += pa[0]
    obj2.innerHTML += "     "
    obj2.innerHTML += " : "
    obj2.innerHTML += pa[1]  
}
  for (let i = 0; i < s.length; i++)
  {
    if (allsb.includes(s[i]) === false)
{
    allsb +=s[i];
}
  }
  let output = "";

  for (var i = 0; i < srtkiva.length; i++) {
      output +=srtkiva[i].charCodeAt(0).toString(2) + " " ;
      if ( i != srtkiva.length - 1)
      {
        output += "0"
      }
     
  }


class Linknode {
  constructor(name, value, next)
{
  this.name = name
  this.value = value
  this.next = next
}

}
  class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;

    }


append(name, value, ptr) {
  const list = new Linknode(name, value , ptr);
 
  if (! this.head || !this.tail)
  {
    this.head = list
    this.tail = list

    return this;
  }

  this.tail.next = list;
this.tail = list;
 
}
  }
  const list = new LinkedList();
 for ( let i = 0; i < 7; i++)
 {
  let a = iters[i]
  list.append(mass[a][1],iters[i], mass[a][1])
  
 }




function change()
{
 
  index = text.value
  masssort[index][0] = "Chimalpopoca"
  obj2.innerHTML = " Список родственников(сестер): "
  obj2.innerHTML += "<br>"
  for (let pa of masssort) {
  
    obj2.innerHTML += "<br>"
    obj2.innerHTML += pa[0]
    obj2.innerHTML += "     "
    obj2.innerHTML += " : "
    obj2.innerHTML += pa[1]  
}

}

function addit()
{
  index = text1.value
 k = -1;
 for (let pairs of arr)
 {
  k +=1;

  if (index == k){
  obj4.innerHTML += "<br>"
  obj4.innerHTML += ` ${pairs[0]} `
  obj4.innerHTML += ": "
  obj4.innerHTML += ` ${pairs[1]} `

 }
}
}

for (let i = 0; i < mass.length; i++)
{
  sir = mass[i][1]
  if (unicname.includes(sir) === false)
  {
      unicname.push(sir)
  }
}





function gena(){
  obj5.innerHTML = "Сгенерировать числа из последовательности Сильвестра: "
  obj5.innerHTML += "<br>"
 
  obj5.innerHTML += "Введите количество элементов последовательности:"
let N = text2.value
let posl = [1, 2]
console.log(posl)
for (let i = 2; i < N ; i++)
{
  k = posl[i-1]*posl[i-2] + 1;
  posl.push(k)
}

posl = posl.sort(() => Math.random() - 0.5)
obj5.innerHTML += "<br>"
obj5.innerHTML += posl
}



//front

var text = document.getElementById("name2");
let text1 = document.getElementById("name");
let text2 = document.getElementById("name1");

obj.innerHTML += "<br>"
obj.innerHTML += "<br>"
obj.innerHTML += "Средний мой балл: "
obj.innerHTML += (a/arr.size).toFixed(2)
obj.innerHTML += "<br>"
obj.innerHTML += "Общая длина всех названий предметов: "
obj.innerHTML += s.length;
obj.innerHTML += "<br>"
obj.innerHTML += "Уникальные симолы: "
obj.innerHTML += allsb;
obj.innerHTML += "<br>"


kiva.innerHTML += "<br>"
kiva.innerHTML += "<strong>Моя кива по имени<strong> '"
kiva.innerHTML += srtkiva
kiva.innerHTML += "' "
kiva.innerHTML += " <strong>ждет с нетерпением!<strong>"
kiva.innerHTML += "<br>"
kiva.innerHTML += "<strong>Ее бинарное имя: <strong> "
for ( let i = 0; i < output.length; i++)
{
  if (i == 26)
  {
      kiva.innerHTML += "<br>"
  }
kiva.innerHTML += output[i];
}



obj3.innerHTML += "<br>"
obj3.innerHTML += "<br>"
obj3.innerHTML += JSON.stringify(list)


obj.innerHTML += "Уникальные имена: "
obj.innerHTML += unicname

let elem = document.getElementById('temp-text');

elem.innerHTML += "<br>"
elem.innerHTML += myperson.name += " "
elem.innerHTML += myperson.surname

obj5.innerHTML += "Введите количество элементов последовательности:"
