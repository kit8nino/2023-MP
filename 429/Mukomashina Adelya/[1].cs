using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Globalization;
using System.Text;
using System.Xml.Serialization;
//кортеж с личной информацией
(string, int, int, int) person = ("Mukomashina Adelya Raisovna", 3, 12, 2003);

// словарь-аттестат
var attestat = new Dictionary<string, int>()
{
    {"Русский язык", 5},
    {"Литература", 4},
    {"Английский язык", 4},
    {"Немецкий язык", 4},
    {"Алгебра", 4},
    {"Геометрия", 4},
    {"Информатика", 5},
    {"История России", 4},
    {"Всеобщая история", 5},
    {"Обществознание", 4},
    {"География", 4},
    {"Биология", 4},
    {"Физика", 4},
    {"Химия", 4},
    {"Музыка", 5},
};

//список родственников
List<string> rodnya = new List<string>() { "Alsu", "Rais", "Roziya", "Anver", "Kamilya", "Rustam", "Alsu" };

// строка с именем моей пушистой кивой
string kiva = "Abrikosik";
double summ = 0;
int item = 0;

//1
foreach (var ball in attestat)
{
    summ += ball.Value;
    item += 1;
}

Console.WriteLine($"Средняя оценка в аттестате: {summ / item}");

//2
var unique = rodnya.Distinct().ToList();
Console.WriteLine($"Уникальные имена среди моих родственников и меня:\n {person.Item1}");
foreach (string s in unique)
    Console.WriteLine(s);
Console.WriteLine("Вывод имен родственников: ");
int dlina1 = 0;
foreach (var name in rodnya)
{
    Console.WriteLine(name);
    dlina1 += name.Length;
}

//3
int dlina = 0;
foreach (var length in attestat)
{
    dlina += length.Key.Length;
}
Console.WriteLine($"Oбщая длина всех названий предметов: {dlina}");

//4
Console.WriteLine("Уникальные буквы в названиях предметов: ");
int i = 0;
foreach (var letters in attestat)
{
    var newstr = String.Join("", letters.Key.Distinct());
    Console.WriteLine($"{i}. {letters.Key} - {newstr}");
    i++;
}

//5
StringBuilder sb = new StringBuilder(); //dynamic string
foreach (byte b in System.Text.Encoding.Default.GetBytes(kiva))
{
    sb.Append(Convert.ToString(b, 2).PadLeft(8, '0')); //padleft - слева дополняется ноликами до длины строки 8
}
Console.WriteLine($"Имя моей домашней пушистой кивы в бинарном виде: {sb}");

//6
List<string> people = new List<string>(rodnya);
people.Sort();
people.Reverse();
Console.WriteLine("Oтсортированный по алфавиту (в обратном порядке) список родственников: ");
foreach (var name in people) Console.WriteLine(name);

//7
DateTime now = DateTime.Now;
DateTime date2 = new DateTime(2003, 12, 03);
Console.WriteLine($"Количество дней и времени от моей даты рождения до текущей даты : {now.Subtract(date2).Days}");

//8
List<string> prethings = new List<string>();
foreach (var prething in attestat) prethings.Add(prething.Key);
Queue<string> things = new Queue<string>();
Console.WriteLine("Введите индекс предмета, который хотите добавить в очередь fifo(для остановки наберите на клавиатуре число >15): ");
int thing = Convert.ToInt32(Console.ReadLine());
while (thing < 15)
{
    things.Enqueue(prethings[thing]);
    thing = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("Предметы из очереди: ");
foreach (string ii in things) Console.WriteLine(ii);

//9
string[] names_of_rulers = {"Tenoch", "Acamapochtli", "Huitzilihitl", "Chimalpopoca", "Xihuitl Temoc",
            "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc"};
int number = (person.Item2 + Convert.ToInt32(Math.Pow(person.Item3, 2)) + person.Item4) % 21 + 1;
Console.WriteLine($"Номер ацтекского правителя: {number}, тогда это имя: {names_of_rulers[number]}");
Console.WriteLine("Введите индекс родственника от 0 до 6, имя которого вы хотите поменять: ");
int index = Convert.ToInt32(Console.ReadLine());
if (index < 0 && index > 6)
    Console.WriteLine("error!");
else
{
    people[index] = names_of_rulers[number];
    Console.WriteLine("Измененный список имен родственников: ");
    foreach (var name in people) Console.WriteLine(name);
}

//10
var relatives = new Dictionary<string, DateTime>();
string name_member_of_family;
DateTime userDateTime;
do
{
    Console.WriteLine("Введите имя родственника(или цифру для выхода): ");
    name_member_of_family = Console.ReadLine();
    if (name_member_of_family.All(char.IsLetter))
    {
        Console.WriteLine("Введите дату рождения родственника: ");
        DateTime.TryParse(Console.ReadLine(), out userDateTime);
        relatives[name_member_of_family] = userDateTime;
    }
    else
    {
        relatives = relatives.OrderBy(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
        Console.WriteLine("Вы остановили ввод родственников. Словарь родственников:  ");
        foreach (var name in relatives) Console.WriteLine(name);
    }

} while (name_member_of_family.All(char.IsLetter));

//11
//Определение варианта
string[] varients = { "аликвотная последовательность", "последовательность Сильвестра", "числа трибоначчи", "числа Леонардо" };
int choice = person.Item1.Length * dlina1 % 4;
Console.WriteLine($"Мой вариант: {varients[choice]}");
Console.WriteLine("Введите число, для которого вы хотите сделать аликвотную последовательность: ");
number = Convert.ToInt32(Console.ReadLine());
var numbers = new List<int>();
Console.WriteLine($"Аликвотная последовательность для числа {number} - ");
aliquot_sequence(number);
void aliquot_sequence(int number)
{
    if (number == 0)
        return;
    int sum = 0;
    for (int i = 1; i < number; i++)
        if(number% i == 0)
            sum+= i;
    Console.WriteLine(sum);
    aliquot_sequence(sum);
}
