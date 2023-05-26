const canvas =document.querySelector('canvas')
const c = canvas.getContext('2d')
canvas.width = 730;
canvas.height = 730;
cells = 48;
let random;
let tracx = 0;
let tracy = 0;
let brx = 0;
let bry = 0;
let l = 400;
let l2 = 400;
let u, v, u1, u2, it1, it2, s;
let winx, winy, winx2, winy2;
const matrix = matrixy(16, 16);

matrix[0][0] = 1;

console.log(matrix)


function matrixy(a , b) {
 const matrix = [];
    for (let y= 0 ; y < b; y++)
    {
        const b = [];
        for (let x = 0; x < a; x++ ) {
        b.push(0);
        }
        matrix.push(b)
    }
    return matrix;
}



function ris()

{
    c.fillStyle = "red"
drawexit(0,0)
    for (let x = 0; x < 4000; x++) {
    let u;

if (matrix[tracy][tracx] == 1 )
{
 
   u =  Math.trunc(Math.random()*(5-1) + 1)
   

switch(u)
{
case 3:
    if( tracx+2 <=15 )
    {
        tracx+=2;
        if (matrix[tracy][tracx] == 0) {
 matrix[tracy][tracx] = 1
 matrix[tracy][tracx-1] = 1
 drawcell(tracx*cells,tracy*cells)
 drawcell((tracx-1)*cells,tracy*cells )
    }
}

 break;
case 1:
    if ( tracx-2 >= 0  )
tracx-=2;
if (matrix[tracy][tracx] == 0) {
matrix[tracy][tracx] = 1
matrix[tracy][tracx+1] = 1
drawcell(tracx*cells,tracy*cells)
drawcell((tracx+1)*cells,tracy*cells )
}
  break;
 case 2:
    if( tracy+2 <=15  )
 tracy+=2;
 if (matrix[tracy][tracx] == 0) {
 matrix[tracy][tracx] = 1
 matrix[tracy-1][tracx] = 1
 drawcell(tracx*cells,tracy*cells)
 drawcell(tracx*cells,(tracy-1)*cells )
 }
 break;
case 4:
    if(tracy-2 >= 0)
tracy-=2;
if (matrix[tracy][tracx] == 0) {
matrix[tracy][tracx] = 1
matrix[tracy+1][tracx] = 1
drawcell(tracx*cells,tracy*cells)
drawcell(tracx*cells,(tracy+1)*cells )
 break;
}
}


c.fillStyle = "blue"
    drawexit(14*cells,10*cells)


if(x == 3999)
{
    matrix[3][11] = 1;
    drawcell(11*cells, 3*cells)
    matrix[3][10] = 1;
    drawcell(10*cells, 3*cells)
    matrix[5][7] = 1;
    drawcell(7*cells, 5*cells)
    matrix[6][7] = 1;
    drawcell(7*cells, 6*cells)
    matrix[4][8] = 1;
    drawcell(8*cells, 4*cells)
    matrix[4][7] = 1;
    drawcell(7*cells, 4*cells)
    matrix[3][5] = 1;
    drawcell(5*cells, 3*cells)
    matrix[4][5] = 1;
    drawcell(5*cells, 4*cells)
    matrix[12][7] = 1;
   drawcell(7*cells, 12*cells)
   matrix[12][6] = 1;
   drawcell(6*cells, 12*cells)
   matrix[0][7] = 1;
   drawcell(7*cells, 0*cells)
   matrix[0][8] = 1;
   drawcell(8*cells, 0*cells)
   matrix[7][7] = 1;
   drawcell(7*cells, 7*cells)
   matrix[7][8] = 1;
   drawcell(8*cells, 7*cells)
   matrix[3][4] = 1;
   drawcell(4*cells, 3*cells)

   matrix[tracy][tracx] = "c";
   winx = tracx ;
   winy = tracy  
   winx2 = tracx ;
   winy2 = tracy  
    drawchest(tracx*cells,tracy*cells)
}
}
}
}

function broditel()
{
    if (matrix[0][0] == 1)
    {
        if (matrix[0][1] == 1)
        {
            matrix[0][1] = 2
        }
        if (matrix[1][0] == 1)
        {
        matrix[1][0] = 2
        }
    }
    matrix[0][0] ="y";

for (let k = 2; k < 100; k++)
{
    for ( let y = 0; y < 15; y++)
    {
        for (let x = 0; x < 15; x++)
        {
            if (matrix[y][x] == k)
            {
                
               
                if (matrix[y][x+1] == 1)
                {
                    matrix[y][x+1] = k+1;
                }
                if (matrix[y][x-1] == 1)
                {
                    matrix[y][x-1] = k+1;
                }
                if(y+1 <15) {
                if (matrix[y+1][x] == 1)
                {
                matrix[y+1][x] = k+1;
                }
            }
                if(y-1 >=0) {
                if (matrix[y-1][x] == 1)
                {
                matrix[y-1][x] = k+1;
                }
            }
            }
        }
    }
          
           
        
       
     
}
}

function broditel2()
{
    if (matrix[10][14] == 1)
    {
        
        
        if (matrix[11][14] == 1)
        {
        matrix[11][14] = 2
        }
        if (matrix[9][14] == 1)
        {
        matrix[9][14] = 2
        }
        if (matrix[10][13] == 1)
        {
        matrix[10][13] = 2
        }
    }
    matrix[10][14] ="v";

for (let k = 2; k < 100; k++)
{
    for ( let y = 0; y < 15; y++)
    {
        for (let x = 0; x < 15; x++)
        {
            if (matrix[y][x] == k)
            {
                
                drawpath(x*cells, y*cells);
                if (matrix[y][x+1] == 1)
                {
                    matrix[y][x+1] = k+1;
                }
                if (matrix[y][x-1] == 1)
                {
                    matrix[y][x-1] = k+1;
                }
                if(y+1 <15) {
                if (matrix[y+1][x] == 1)
                {
                matrix[y+1][x] = k+1;
                }
            }
                if(y-1 >=0) {
                if (matrix[y-1][x] == 1)
                {
                matrix[y-1][x] = k+1;
                }
            }
            }
        }
    }
          
           
        
       
     
}
}

function pather(){
 u = winx;
 v = winy;
    for (let i = 0; i < 50; i++) {
winx = u;
winy = v;

    if (matrix[winy][winx+1] < l && matrix[winy][winx+1] !=0 && winx+1 < 15  && matrix[winy][winx+1] !=1)
    {
   l = matrix[winy][winx+1];
   u = winx+1;
   v = winy;
    }
    if (matrix[winy][winx-1] < l && matrix[winy][winx-1] !=0 && winx-1 >=0  && matrix[winy][winx-1] !=1)
    {
    l = matrix[winy][winx-1];
    u = winx-1;
    v = winy;
     }
     if ( winy != 0) {
    if (matrix[winy-1][winx] < l && matrix[winy-1][winx] !=0 && winy-1 >=0 && matrix[winy-1][winx] !=1)
    {
    l = matrix[winy-1][winx];
    u = winx;
    v = winy-1;
     }
     }

    if (matrix[winy+1][winx] < l && matrix[winy+1][winx] !=0 && winy+1 <15 && matrix[winy+1][winx] !=1)
    {
    l = matrix[winy+1][winx];
    u = winx;
    v = winy+1;
     }
     if ( i == 0) {
        it1 = l;
    console.log(l, " ", u, " ", v)
     }
    drawarc(u*cells,v*cells)

    }
   
}

function clear(){
    for (let y = 0; y < 16; y++)
    {
        for (let x = 0; x < 15; x++)
        {
            if (matrix[y][x] !=0 && matrix[y][x] !="y" && matrix[y][x] !="c")
            {
                matrix[y][x] = 1;
            }
        }
    }
}

function pather2()
{

    u2 = winx2;
    v2 = winy2;
    console.log(winx2)
       for (let i = 0; i < 50; i++) {
   winx2 = u2;
   winy2= v2;
   
       if (matrix[winy2][winx2+1] < l2 && matrix[winy2][winx2+1] !=0 && winx2+1 < 15  && matrix[winy2][winx2+1] !=1)
       {
      l2 = matrix[winy2][winx2+1];
      u2= winx2+1;
      v2 = winy2;
       }
       if (matrix[winy2][winx2-1] < l2 && matrix[winy2][winx2-1] !=0 && winx2-1 >=0  && matrix[winy2][winx2-1] !=1)
       {
       l2 = matrix[winy2][winx2-1];
       u2 = winx2-1;
       v2 = winy2;
        }
        if ( winy2 != 0) {
       if (matrix[winy2-1][winx2] < l2 && matrix[winy2-1][winx2] !=0 && winy2-1 >=0 && matrix[winy2-1][winx2] !=1)
       {
       l2 = matrix[winy2-1][winx2];
       u2 = winx2;
       v2 = winy2-1;
        }
        }
   
       if (matrix[winy2+1][winx2] < l2 && matrix[winy2+1][winx2] !=0 && winy2+1 <15 && matrix[winy2+1][winx2] !=1)
       {
       l2 = matrix[winy2+1][winx2];
       u2 = winx2;
       v2 = winy2+1;
        }
        if ( i == 0)
        {
       console.log(l2, " ", u2, " ", v2)
       it2 = l2;
        }
       drawarc2(u2*cells,v2*cells)
       
       }
    
}


drawblock();
drawcell(0, 0)

ris();
broditel();
pather();

clear();
broditel2();
pather2();
itog()

function itog() {

console.log(it1, "- to the chest;    ", it2, "- to the exit;    ", it1+it2, "- All path;")

}
function drawblock() {
    c.fillStyle = "black"
    c.fillRect(0, 0 , canvas.width, canvas.height);
}

function drawcell(a, b)
{
    c.fillStyle =  "white"
    c.fillRect(a+5, b+5, cells, cells)
}

function drawchest(a, b)
{
    c.fillStyle =  "yellow"
    c.fillRect(a+5, b+5, cells, cells)
}

function drawexit(a, b)
{
    c.fillRect(a+5, b+5, cells, cells)
}
function drawpath(a,b){
    c.fillStyle = "rgb(12, 180, 65, 0.01)";
    c.fillRect(a+5, b+5, cells, cells)
}

function drawarc(a, b)

{
    c.fillStyle = "red"
    c.fillRect(a+20, b+15, 10, 10)
}
function drawarc2(a, b)

{
    c.fillStyle = "blue"
    c.fillRect(a+20, b+30, 10, 10)
}