#include <iostream>
#include <vector>
#include <tuple>
#include <map>
#include <list>
#include <iterator>
#include <bitset>
#include <ctime>
#include <queue>
#include <string>

void Tribonachi(int x1, int x2, int x3, int y, int z, int lim)
{   
    if(y < lim)
    {

        std::cout << z << " : " << y << "\n";
        z++;
        y = x1 + x2 + x3;
        return Tribonachi(y, x1, x2, y, z, lim);

    }


}

//Личная информация
std::tuple<std::string, std::string, std::string, int, int, int> my_data("Комаров", "Никита", "Александрович", 28, 8, 2002);

//Аттестат
std::map<std::string, int> attestate
{

    {"Алгебра",4},
    {"Геометрия",4},
    {"Физическая культура",5},
    {"Английский язык",5},
    {"География",4},
    {"Литература",4},
    {"Русский язык",4},
    {"История России",5},
    {"Химия",5},
    {"Физика",4},
    {"Информатика",5},
    {"Обществознание",4},
    {"ОБЖ",5},
    {"Всеобщая История",4},
    {"Технология",5},

};

//Список родственников
std::string list[] { "Александр", "Роман", "Александр", "Елена", "Ксения", "Савелий", "Галина", "Алексей" };

//Имя моей кивы
std::string Kiwa = "Shumatsu";

int main()
{
    setlocale(0, "");
    
   //1
    double Av_Mark, sum = 0, kolvo = 0;

    for (auto& ball : attestate)
    {
        sum += ball.second;
        kolvo++;
    }

    Av_Mark = sum / kolvo;
    std::cout << "Средняя оценка : " << Av_Mark << std::endl << std::endl;

    //2
    std::cout << "Уникальные имена: ";

    for (std::string s : list)
    {
        std::string name = s;
        int unique = std::count(std::begin(list), std::end(list), name);
        if (unique == 1)
            std::cout << s << " ";
        unique = 0;
    }
    std::cout << std::get<1>(my_data);
    std::cout << std::endl << std::endl;

    //3
    int dlina = 0;
    for (auto item : attestate)
        dlina += item.first.size();
    std::cout << "Oбщая длина всех названий предметов : " << dlina << std::endl << std::endl;

    //4
    char keys[255];
    std::string all_items;

    for (auto item : attestate)
        all_items += item.first;

    strcpy_s(keys, all_items.c_str());

    std::cout << "уникальные буквы в названиях предметов : ";

    for (char ch : keys)
    {
        
        int unique = std::count(std::begin(keys), std::end(keys), ch);

        if (unique == 1)
            std::cout << ch << " ";
        unique = 0;

    }
    std::cout << std::endl << std::endl;

    //5
    std::cout << "имя моей домашней пушистой кивы в бинарном виде : ";

    for (char const& c : Kiwa)
        std::cout << std::bitset<8>(c) << ' ';

    std::cout << std::endl << std::endl;

    //6
    int list_size = 0;
    for (auto s : list)
        list_size += 1;

    for (int i = 0; i < list_size; i++)
    for (int j = i + 1; j < list_size; j++)
        if (list[i]<list[j])
            std::swap(list[i], list[j]);
    std::cout << "отсортированный по алфавиту (в обратном порядке) список родственников : ";

    for (auto s : list)
        std::cout << s << " ";
    std::cout << std::endl << std::endl;

    //7
    time_t rawtime;
    time(&rawtime);
    int days = 0;
    days += 1970 * 365 + time(&rawtime) / 60 / 60 / 24 - std::get<5>(my_data) * 365 + std::get<4>(my_data) * 30 + std::get<3>(my_data);
    std::cout << "количество дней от моей даты рождения до текущей даты : " << days << std::endl << std::endl;

    //8
    std::cout << "FIFO : ";

    std::queue<std::string> stuff;

    std::string inp;
    std::cin >> inp;

    while (inp != "-1")
    {

        stuff.push(inp);
        std::cin >> inp;

    }
    std::cout << "Вывод: ";


    while (!stuff.empty())  
    {
        std::cout << stuff.front() << " ";
        stuff.pop();    
    }
    std::cout << std::endl << std::endl;
    //9
    int number = (std::get<3>(my_data) + std::get<4>(my_data)*std::get<4>(my_data) + std::get<5>(my_data)) % 21 + 1;
                 //№16 - Xochiquentzin
    std::string aztec = "Xochiquentzin";

    std::cout << "Введите индекс(0-8): ";
    int ind;
    std::cin >> ind;
    list[ind] = aztec;
    std::cout << "Имена родственников: ";
    for(std::string s : list)
        std::cout << s << " ";

    std::cout << std::endl << std::endl;

    //10
    class Node {
    public:
        std::string data;
        int _index;
        Node* next;

    public:
        Node(std::string data, int _index) {
            this->_index = _index;
            this->data = data;
            this->next = NULL;
        }
    };
    
    class OneLinkedList {
    public:
        Node* head, * tail;

    public:
        int _indexL = 0;

        OneLinkedList() {
            this->head = this->tail = NULL;
        }

        ~OneLinkedList() {
            while (head != NULL) pop_front();
        }

        void pop_front() {
            if (head == NULL) return;

            if (head == tail) {
                delete tail;
                head = tail = NULL;
                return;
            }

            Node* node = head;
            head = node->next;
            delete node;
        }

        void push_back(std::string data) {
            Node* node = new Node(data, _indexL);
            if (head == NULL) head = node;
            if (tail != NULL) tail->next = node;
            tail = node;
            _indexL++;
        }

        void push_front(std::string data) {
            Node* node = new Node(data, _indexL);
            node->next = head;
            head = node;
            if (tail == NULL) tail = node;
            _indexL++;
        } 

        void pop_back() {
            if (tail == NULL) return;
            if (head == tail) {
                delete tail;
                head = tail = NULL;
                return;
            }

            Node* node = head;
            for (; node->next != tail; node = node->next);

            node->next = NULL;
            delete tail;
            tail = node;
        }

        Node* getAt(int k) {
            if (k < 0) return NULL;

            Node* node = head;
            int n = 0;
            while (node && n != k && node->next) {
                node = node->next;
                n++;
            }

            return (n == k) ? node : NULL;
        }

    };

    std::vector<std::pair<std::string, int>> ml
    {
    
        {"Савелий",2001},
        {"Ксения",1990},
        {"Елена",1976},
        {"Александр",1970},
        {"Алексей",1981},
        {"Роман",1965},
        {"Галина", 1950},

    };
    
    std::sort(ml.begin(), ml.end(), [](const auto& l1, const auto& l2) { return l1.second < l2.second; });

    OneLinkedList lst;

    for (const auto& name : ml)
        lst.push_back(name.first);

    for (Node* node = lst.head; node != NULL; node = node->next) {
        std::cout << node->data << "[" << node->_index << "]" << " ";
    }
    
    std::cout << std::endl << std::endl;

    //11
    int len_FIO = std::get<0>(my_data).size() + std::get<1>(my_data).size() + std::get<2>(my_data).size();

    int len_family_names = 0;
    for (auto name : list)
        len_family_names += name.size();

    int _number = len_FIO * len_family_names % 4;
    //Вывод - 2(числа Трибоначчи)

    std::cout << "Функция-генератор \n\n" << "Введите предел: ";
    int x1 = 1,
        x2 = 0,
        x3 = 0,
        y  = 0,
        z  = 3,
        lim;

    std::cin >> lim;
    
    //начало
    std::cout << "0 : " << 0 << "\n" << "1 : "<< 0 << "\n" << "2 : " <<  1 << "\n";

    Tribonachi(1, 0, 0, 0, 3, lim);


}


