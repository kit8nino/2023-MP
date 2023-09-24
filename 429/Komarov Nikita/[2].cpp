#include <iostream>
#include <algorithm>
#include <random>
#include <complex>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

/* for(i = 0; i < 4; i++)
     std::cout << rand() % 18 + 1;

    random => 2,10,5,4
*/
//Пузырьковая сортировка(2)
void bubbleSort(std::vector<int>& a)
{
    bool swapp = true;
    while (swapp) {
        swapp = false;
        for (size_t i = 0; i < a.size() - 1; i++) {
            if (a[i] > a[i + 1]) {
                a[i] += a[i + 1];
                a[i + 1] = a[i] - a[i + 1];
                a[i] -= a[i + 1];
                swapp = true;
            }
        }
    }
}

//Сортировка вставками(4)
void insertionSort(std::vector<double>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        double key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

//Сортировка Шелла(5)
void shellSort(std::vector<std::complex<double>>& arr) {
    for (int gapSize = arr.size() / 2; gapSize > 0; gapSize /= 2) {
        for (size_t currentIndex = gapSize; currentIndex < arr.size(); currentIndex++) {
            int currentIndexCopy = currentIndex;
            double item = std::abs(arr[currentIndex]);

            while (currentIndexCopy >= gapSize && std::abs(arr[currentIndexCopy - gapSize]) > item) {
                arr[currentIndexCopy] = arr[currentIndexCopy - gapSize];
                currentIndexCopy -= gapSize;
            }

            arr[currentIndexCopy] = item;
        }
    }
}

//Быстрая сортировка(10)
void quickSort(std::string& str, int left, int right) {
    int i = left, j = right;
    int mid = str[(left + right) / 2];

    /* partition */
    while (i <= j) {
        while (str[i] < mid)
            i++;
        while (str[j] > mid)
            j--;
        if (i <= j) {
            std::swap(str[i], str[j]);
            i++; j--;
        }
    };

    /* recursion */
    if (left < j)
        quickSort(str, left, j);
    if (i < right)
        quickSort(str, i, right);
}

std::vector<int> integer_nums;                      //Массив целых чисел
std::vector<double> real_nums;                      //Массив вещественных чисел
std::vector<std::complex <double> > complex_nums;   //Массив комплексных чисел
std::string str;                                    //Массив строк для текста из файла

//База
int main()
{
    setlocale(0, "");
    //Заполнение массива целых чисел(integer_nums)
    for (int i = 0; i < 1000000; i++)
        integer_nums.push_back(rand());

    //Заполнение массива вещественных чисел(real_nums)
    double min = -1.;
    double max = 1.;
    for (int i = 0; i < 100000; i++)
        real_nums.push_back(min + (double)rand() * (max - min) / (double)RAND_MAX);

    //Объявление r
    double r = 28. / 8.;

    //Заполнение массива комплексных чисел(complex_nums)
    double x, y, z;
    for (int i = 0; i < 42000; i++) {

        x = (double)rand() * (r + r) - r;
        y = (double)rand() * (r + r) - r;
        z = sqrt(x * x + y * y);
        if (z < r)
            complex_nums.push_back(std::complex<double>(x, y));
    }

    //Заполняем наш массив строк str из файла
    std::ifstream file("C:\\Users\\berkl\\Desktop\\Text2.txt");
    if (file.is_open())
    {
        std::ostringstream ss;
        ss << file.rdbuf();
        str = ss.str();
    }
    file.close();
    
    //Удаляем символы пунктуации
    for (int i = 0, len = str.size(); i < len; i++)
    {
        if (ispunct(str[i]))
        {
            str.erase(i--, 1);
            len = str.size();
        }
    }
    //std::cout << str;

    //Применяем сортировки к массивам данных
    bubbleSort(integer_nums);
    insertionSort(real_nums);
    shellSort(complex_nums);
    quickSort(str, 0, str.size()-1);

    
}
