//изменить путь к файлу с отрывком из книги!
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Drawing;
using System.Numerics;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;
using System.Xml.Linq;
//4 случайных номера сортировки
Random randon = new Random();
//for (int ctr = 0; ctr < 4; ctr++)
//{
//    Console.Write("{0,3}   ", randon.Next(1, 19));
//}
//выпало: 1, 5, 18, 11
//ввести можно от 1 до 4, так как на выбор 4 метода

//список целых чисел от 0 до 999999 c mergesort
List<int> list1 = new List<int>();
for(int i = 0; i < 1000000; i++)
{
    list1.Add(i);
}


//список из 99999 случайных вещественных чисел в диапазоне [-1, 1] c shellsort
List<double> list2 = new List<double>();
Random rnd = new Random();
for (int i = 0;i < 100000; i++)
{
    list2.Add(rnd.NextDouble() * 2 - 1);
}
//42000 разных точки комплексной плоскости, лежащие внутри окружности
//радиуса r = birth_day / birth_month (можно случайных, можно равномерно
//распределённых), сортировать по модулю числа; c shakersort
double birth_day = 3.0;
int birth_month = 12;
double r = birth_day / birth_month;
List<Complex> list3 = new List<Complex>();
while (list3.Count < 6)
{
    var rand = new Random();
    var x = rand.NextDouble() * (r + r) - r;
    var y = rand.NextDouble() * (r + r) - r;
    if(Math.Sqrt(x*x + y*y) <= r)
    {
        Complex complexNumber = new Complex(x, y);
        list3.Add(complexNumber);
    }
}
list3.Sort((x, y) => (x.Magnitude.CompareTo(y.Magnitude)));

//отрывок из книги (любой, на свой выбор) не менее 10000 слов,
//разбитый в список по словам c timsort
List<String> phrases = new List<string>();
List<String> words = new List<string>();
using (StreamReader sr = new StreamReader(@"C:\Users\MyPC\Desktop\2023-MP\429\Mukomashina Adelya\petSematary.txt"))
{
    while (!sr.EndOfStream)
    {
        phrases.Add(sr.ReadLine());
    }
    for (int i = 0; i < phrases.Count; i++)
    {
        if (phrases[i].Length == 0) continue;
        string[] word = phrases[i].Split(' ');
        foreach(var j in word)
            words.Add(j);
    }
}


Console.WriteLine("Choose one of sorting methods(1(1),2(5),3(11),4(18)): ");
int numberOfMethod = Convert.ToInt32(Console.ReadLine());
switch (numberOfMethod)
{
    case 1:
        shakerSort(list3);
        break;
    case 2:
        shellSort(list2);
        break;
    case 3:
        MergeSort(list1);
        break;
    case 4:
        timsort(words);
        break;
    default:
        Console.WriteLine("Введите число от 1 до 4");
        break;
}




//Shaker sort
static void shakerSort(List<Complex> list)
{
    Random rnd = new Random();
    //random with list
    for (int i = list.Count - 1; i >= 1; i--)
    {
        int j = rnd.Next(i + 1);
        var temp = list[j];
        list[j] = list[i];
        list[i] = temp;
    }
    foreach (Complex i in list)
        Console.Write(i + " ");

    //beginning of the Shaker sort
    int left = 0;
    int right = list.Count - 1;

    while (left < right)
    {
        for (int i = left; i < right; i++)
            if (Complex.Abs(list[i]) > Complex.Abs(list[i + 1]))
            {
                (list[i], list[i + 1]) = (list[i + 1], list[i]);
            }
                
        right--;
        for (int i = right; i > left; i--)
            if (Complex.Abs(list[i-1]) > Complex.Abs(list[i]))
                (list[i - 1], list[i]) = (list[i], list[i - 1]);
        left++;
    }
    Console.WriteLine();
    Console.WriteLine("result of sort: ");
    Console.WriteLine();
    foreach (Complex i in list)
        Console.Write(i + " ");
}




//Shellsort
static void shellSort(List<double> list)
{
    int l = 0;
    int ri = list.Count;
    int step = ri / 2;
    while (step > 0)
    {
        for (int i = l + step; i < ri; i++)
        {
            int j = i;
            int diff = j - step;
            while (diff >= l && list[diff] > list[j])
            {
                (list[diff], list[j]) = (list[j], list[diff]);
                j = diff;
                diff = j - step;
            }
        }
        step /= 2;
    }
    Console.WriteLine("result of sort: ");
    Console.WriteLine();
    foreach (double i in list)
        Console.Write(i + " ");

}


//Merge sort
static void MergeSort(List<int> list)
{
    Console.WriteLine();
    Console.WriteLine("result of sort: ");
    int l = 0;
    int ri = list.Count - 1;
    mergeSort(list, l, ri);
    Console.WriteLine();
    foreach (int i in list)
        Console.Write(i + " ");
}

static void merge(List<int> list, int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    List<int> left = new List<int>(new int[n1 + 1]);
    List<int> right = new List<int>(new int[n2 + 1]);

    for (i = 0; i < n1; i++)
    {
        left[i] = list[l + i];

    }
    for (j = 1; j <= n2; j++)
    {
        right[j - 1] = list[m + j];
    }
    left[n1] = int.MaxValue;
    right[n2] = int.MaxValue;
    i = 0;
    j = 0;
    for (k = l; k <= r; k++)
    {
        if (left[i] < right[j])
        {
            list[k] = left[i];
            i++;
        }
        else
        {
            list[k] = right[j];
            j++;
        }
    }
}
static void mergeSort(List<int> list, int l, int r)
{
    int q;
    if (l < r)
    {
        q = (l + r) / 2;
        mergeSort(list, l, q);
        mergeSort(list, q + 1, r);
        merge(list, l, q, r);
    }
}


//timsort
static void timsort(List<string> arr)
{
    timSort(arr, arr.Count);
    Console.WriteLine();
    foreach (string i in arr)
        Console.Write(i + " ");
}

static void insertionSort(List<string> arr, int left, int right)
{
    for (int i = left + 1; i <= right; i++)
    {
        string temp = arr[i];
        int j = i - 1;
        while (j >= left && string.Compare(arr[j], temp) < 0)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}

static void mergeI(List<string> arr, int l, int m, int r)
{
    int len1 = m - l + 1, len2 = r - m;
    List<string> left = new List<string>(new string[len1 + 1]);
    List<string> right = new List<string>(new string[len2 + 1]);
    for (int z = 0; z < len1; z++)
        left[z] = arr[l + z];
    for (int z = 0; z < len2; z++)
        right[z] = arr[m + 1 + z];

    int i = 0;
    int j = 0;
    int k = l;

    while (i < len1 && j < len2)
    {
        if (string.Compare(left[i], right[j]) >= 0)
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < len1)
    {
        arr[k] = left[i];
        k++;
        i++;
    }

    while (j < len2)
    {
        arr[k] = right[j];
        k++;
        j++;
    }
}

static void timSort(List<string> arr, int n)
{
    for (int i = 0; i < n; i += 32)
        insertionSort(arr, i, Math.Min((i + 32 - 1), (n - 1)));

    for (int size = 32; size < n; size = 2 * size)
    {
        for (int left = 0; left < n; left += 2 * size)
        {
            int mid = left + size - 1;
            int right = Math.Min((left + 2 * size - 1), (n - 1));

            if (mid < right)
                mergeI(arr, left, mid, right);
        }
    }
}
