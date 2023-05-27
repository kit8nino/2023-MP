#include <iostream>
#include <tuple>
#include <string>
#include <map>
#include <list>
#include <vector>
#include <algorithm>
#include <set>
#include <bitset>
#include <ctime>
#include <queue>
#include < Windows.h >

#pragma warning(disable : 4996)
using namespace std;

int main()
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "Russian");
	//Исходные данные
	// Кортеж
	tuple<string, string, string, string, string, string >Info;
	Info = make_tuple("Утросин", "Кирилл", "Сергеевич", "24", "06", "2004");

	// Словарь
	map<string, unsigned> atestat 
	{
		{"Русский", 4}, {"Матан", 4},{"Литература", 3},{"Физра", 4},
		{"История России", 5},{"Всеобщая История", 5},{"Информатика", 5},
		{"Геометрия", 5},{"Физика", 4},{"Химия", 3},{"Изо", 4},
		{"Астрономия", 4},{"Прогулы", 5}, {"Разговоры о важном", 5}
	};

	// Список родственников
	vector<string> relatives{"Мария 1950","Григорий 1994", "Александр 1975", "Павел 1972",
		"Сергей 1971", "Наташа 1983", "Александр 1956", "Михаил 2002", "Дмитрий 2003", "Дмитрий 2007",
		"Галина 1949", "Алина 1955", "Вера 1999", "Антон 1991", "Слава 2001", "Крипер 2004" };
	
	// Кива
	string kiwa = "Мявка";

#pragma region Задание №1
	int avg_mark = 0;
	for (const auto& pair : atestat) 
	{
		avg_mark += pair.second;
	}
	avg_mark = avg_mark / atestat.size();
	cout << "Средняя оценка по аттестату: " << avg_mark << endl;
#pragma endregion
#pragma region Задание №2
	vector<string> rel;
	vector<string> unique_relatives;
	string name;
	string uniq;
	int j = 0;
	cout << "  " << endl;
	for (int i = 0; i < relatives.size(); i++)
	{
		name = relatives[i];
		while (name[j] != ' ') 
		{
			uniq += name[j];
			j += 1;
		}
		rel.push_back(uniq);
		uniq = "";
		j = 0;
	}
	
	uniq = "";
	unique_relatives = rel;

	sort(unique_relatives.begin(), unique_relatives.end());
	unique_relatives.erase(unique(unique_relatives.begin(), unique_relatives.end()), unique_relatives.end());

	for (const auto& x : unique_relatives) 
	{
		cout << x << " ";
	}

	cout << endl;

#pragma endregion
#pragma region Задание №3
	string dlina = "";
	for (const auto& pair : atestat)
	{
		dlina += pair.first;
	}
	cout << "Общая длина всех названий предметов: " << dlina.length() << endl;
#pragma endregion
#pragma region Задание №4
	set<char> unique_letters;
	string letters = "";
	for (const auto& pair : atestat)
	{
		letters += (pair.first);
	}

	cout << "Уникальные буквы в названиях предметов: ";
	for (char letter : letters) {
		unique_letters.insert(letter);
	}
	for (char n : unique_letters)
		cout << n;
	cout << endl;

#pragma endregion
#pragma region Задание №5
	cout << "Имя Мявка в бинарном коде: " << endl;
	for (int i = 0; i < kiwa.size(); i++) {
		cout << bitset<8>(kiwa[i]) << ' ';
	}
	cout << endl;
#pragma endregion
#pragma region Задание №6
	vector<string> sorted_relatives = relatives;
	sort(sorted_relatives.rbegin(), sorted_relatives.rend());

	cout << "Отсортированный в обратном порядке список родственников: " << endl;
	for (const auto& f : sorted_relatives) {
		cout << f << ", ";
	}
	cout << endl;
#pragma endregion
#pragma region Задание №7
	int year = 2003;
	int month = 6;
	int day = 24;

	time_t now = time(0);
	tm* ltm = localtime(&now);

	tm specified_tm = { 0 };
	specified_tm.tm_year = year - 1900;
	specified_tm.tm_mon = month - 1;
	specified_tm.tm_mday = day;

	time_t specified_date = mktime(&specified_tm);
	double diff = difftime(now, specified_date);

	int days = static_cast<int>(diff / (60 * 60 * 24));

	cout << "Разница в днях между др и текущей датой: " << days << endl;


#pragma endregion
#pragma region Задание №8
	queue<string> predm;

	cout << "Введите предметы, 'stop' - остановка:" << endl;

	string input;
	int index = 0;

	while (input != "stop") {
		cin >> input;

		if (input != "stop") {
			predm.push(input);
			cout << "Предмет: '" << input << "' индекс: " << index << endl;
			index++;
		}
	}

	cout << "Введенные предметы:" << endl;

	while (!predm.empty()) {
		cout << predm.front() << endl;
		predm.pop();
	}
#pragma endregion
#pragma region Задание №9
	vector<string> Actec{"Tenoch","Acamapichtli", "Huitzilihuitl", "Chimalpopoca",
		"Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl",
		"Tizoc","Ahuitzotl","Moctezuma II", "Cuitláhuac",
		"Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin",
		"Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac" };
	int number = (day + int(pow(month, 2)) + year) % 21 + 1; //6
	//cout << endl << number;
	
	int Index;
	string Aname;
	cout << "Кого хотите переименовать?: ";
	cin >> Index;
	if (Index >= 0 && Index < sorted_relatives.size()) {
		Aname = Actec[5] + " " + sorted_relatives[index].substr(sorted_relatives[Index].find(' ') + 1);
		sorted_relatives[Index] = Aname;
		cout << "Имя " << sorted_relatives[Index] << " было изменено" << endl;
	}
	else {
		cout << "Индекс вне диапазона" << endl;
	}

#pragma endregion

}
