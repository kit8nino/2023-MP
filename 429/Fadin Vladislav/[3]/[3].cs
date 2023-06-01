/*
Совместо с Кириллом Утросиным (Kirill-U-S)
*/
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Path
{
    class Cell
    {
        public bool isOpen { get; set; }
        public int wmin { get; set; }
        public int vmin { get; set; } //vmin указывает на id клетки к которой минимальный доступный путь 
        public bool isSeen { get; set; }
        public bool isSeenforDepth { get; set; }
        public int id { get; }
        public bool Passed { get; set; }
        public bool PassedDFS { get; set; }

        public bool isKey { get; set; }

        public Cell()
        {

        }
        public Cell(bool isOpen, int wmin, int vmin, int id)
        {
            this.isOpen = isOpen;
            this.wmin = wmin;
            this.vmin = vmin;
            this.id = id;
            Passed = false;
            isSeen = false;
        }
        public void Closed(bool isOpen)
        {
            this.isOpen = isOpen;
        }
        public void Weight(int w, int v)
        {
            if (wmin == 0)
            {
                wmin = w;
                vmin = v;
            }
            else
            {
                if (wmin > w)
                {
                    wmin = w;
                    vmin = v;
                }
            }
        }
    }
    class Program
    {
        static Dictionary<int, Cell> Map = new Dictionary<int, Cell>();
        static List<Cell> PathAll = new List<Cell>();
        static List<Cell> Front = new List<Cell>();
        static string pathtofile = @"maze-for-u.txt";
        static int dlina;
        static int shirina;
        static int idEnter;
        static int idExit;
        static bool text_output;
        /// <summary>
        /// считывает лабиринт
        /// </summary>
        static void ReadFile()
        {
            using (var read = new StreamReader(pathtofile))
            {
                int k = 0;
                while (!read.EndOfStream)
                {
                    List<string> buf = new List<string>();

                    var line = read.ReadLine();
                    dlina = line.Length;
                    for (int i = 0; i < dlina; i++)
                    {
                        int id = k * dlina + i;

                        if (k == 0 && line[i] == ' ')
                            Map.Add(id, new Cell(true, 0, 0, id));
                        else if (line[i] == ' ')
                            Map.Add(id, new Cell(true, 0, 0, id)); //точка доступная к прохождению
                        else if (line[i] == '#')
                            Map.Add(id, new Cell(false, 0, 0, id)); //стена
                    }
                    k++;
                }
                shirina = k;
                for (int i = 0; i < dlina; i++)
                {
                    if (Map[i].isOpen)
                        idEnter = i;
                    if (Map[(shirina - 1) * dlina + i].isOpen)
                        idExit = (shirina - 1) * dlina + i;
                }
            }
        }
        static void Write()
        {
            using (var writer = new StreamWriter(@"maze-for-me-done.txt"))
            {
                foreach (var item in Map)
                {
                    if (item.Value.isKey)
                        writer.Write('*');
                    else if (item.Value.Passed)
                        writer.Write(',');
                    else if (item.Value.PassedDFS)
                        writer.Write('.');
                    else
                        writer.Write(item.Value.isOpen == true ? ' ' : '#');

                    if (item.Key % dlina == dlina - 1)
                        writer.WriteLine();
                }
            }
        }
        /// <summary>
        /// считает вес для клетки id
        /// </summary>
        /// <param name="wa">вес пути из точки аватара</param>
        /// <param name="ps">цена шага</param>
        /// <param name="id">id клетки</param>
        /// <returns></returns>
        static int WÑalc(int wa, int ps, int id)
        {
            int rho = (idExit / dlina - id / dlina)/*вычитаем по i*/ + (idExit % dlina - id % dlina)/*вычитаем по j*/;
            return ps + wa + rho;
        }
        /// <summary>
        /// проверяет наличие Cell в Front
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        static int[] isFront(int id)
        {
            int[] v = new int[2];
            if (Front is null)
            {
                v[0] = 0;
                v[1] = -1;
            }
            else
            {
                bool flag = false;

                //проверка на наличие Cell в Front
                for (int i = 0; i < Front.Count(); i++)
                {
                    if (Front[i].id == id)
                    {
                        flag = true;

                        v[0] = 1;
                        v[1] = i;
                    }
                }

                //если Cell нет во фронте
                if (!flag)
                {
                    v[0] = 0;
                    v[1] = -1;
                }
            }
            return v;
        }
        static List<Cell> A(int idEnter, int idExit)
        {
            List<Cell> Path = new List<Cell>();
            //ставим аватар в начало
            int idcellAvatar = idEnter;

            while (true)
            {
                //вывод в консоль
                if (text_output)
                    Console.WriteLine($"A*: Avatar = {idcellAvatar}, Path.Length: {Path.Count()}");

                Map[idcellAvatar].Passed = true;

                int jk = idcellAvatar % dlina;
                int ik = idcellAvatar / dlina;

                #region расширяем фронт через соседние клетки
                for (int i = -1; i < 2; i++)
                {
                    for (int j = -1; j < 2; j++)
                    {
                        int ii = ik + i;
                        int jj = jk + j;
                        int id = ii * dlina + jj;

                        if (ii >= 0 && jj >= 0)
                        {

                            if (Map[id].isOpen && !Map[id].Passed)//рассматриваем Cell если она не стена и не пройдена аватаром
                            {
                                //считам вес
                                int W = WÑalc(Map[idcellAvatar].wmin, 1, id);

                                //отправляем на добавление
                                Map[id].Weight(W, idcellAvatar);

                                //добавляем во фронт
                                if (!Map[id].isSeen)
                                {
                                    //устанавливаем значение просмотрено
                                    Map[id].isSeen = true;
                                    Front = Front.Append(Map[id]).ToList();

                                    if (text_output)
                                        Console.WriteLine($"Фронт расширен ячейкой: {id}");
                                }
                                else
                                    Front[isFront(id)[1]].Weight(W, idcellAvatar);
                            }
                        }
                    }
                }
                #endregion

                #region ищем Cell с минимальным весом
                int minweight = int.MaxValue;
                int idmin = 0;
                for (int i = 0; i < Front.Count(); i++)
                {
                    if (!Front[i].Passed && Front[i].wmin <= minweight)
                    {
                        minweight = Front[i].wmin;
                        idmin = Front[i].id;
                    }
                }
                #endregion

                idcellAvatar = idmin;
                if (idcellAvatar == idExit)
                    break;
            }

            //обходим лабиринт в обратную сторону по указателям
            //idcellAvatar == idExit    ---->    idEnter
            while (true)
            {
                Path = Path.Append(Map[idcellAvatar]).ToList();
                if (idcellAvatar == idEnter)
                    break;
                idcellAvatar = Map[idcellAvatar].vmin;
            }

            //получили путь => теперь надо перевернуть
            Path.Reverse();
            return Path;
        }

        static int DFS(List<Cell> Path, int idcellAvatar, Dictionary<int, Cell> ToVisit, int idExit)
        {
            ToVisit[idcellAvatar].isSeenforDepth = true;
            Path.Add(ToVisit[idcellAvatar]);

            //вывод в консоль
            if (text_output)
                Console.WriteLine($"DFS: Avatar = {idcellAvatar}, Path.Length: {Path.Count()}");

            #region расширяем фронт через соседние клетки
            int jk = idcellAvatar % dlina;
            int ik = idcellAvatar / dlina;
            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    int ii = ik + i;
                    int jj = jk + j;
                    int id = ii * dlina + jj;

                    int flag = 0;
                    if (id == idExit)
                    {
                        ToVisit[id].isSeenforDepth = true;
                        Path.Add(ToVisit[id]);
                        return -2;
                    }

                    if (ii >= 0 && jj >= 0 && ToVisit.ContainsKey(id) && flag != -1)
                    {
                        if (!ToVisit[id].isSeenforDepth)
                        {
                            ToVisit[id].vmin = idcellAvatar;
                            flag = DFS(Path, id, ToVisit, idExit);

                            if (flag == -2)
                                return -2;
                        }
                    }

                    if (flag == -1)
                    {
                        Path.Remove(Path[Path.Count() - 1]);
                        return -1;
                    }
                }
            }
            #endregion
            Path.Remove(Path[Path.Count() - 1]);
            return 0;
        }
        static void Main(string[] args)
        {
            ReadFile();
            List<Cell> bufPathdfs = new List<Cell>();
            List<int> Keys = new List<int>();
            //выводить ли шаги в консоль
            Console.WriteLine("Выводить шаги в консоль? Y/N");
            string outp = Console.ReadLine();
            if (outp[0] == 'Y')
                text_output = true;
            else if (outp[0] == 'N')
                text_output = false;
            else
                Console.WriteLine("Не ясно -> Программа начала свое действие");

            //В глубину
            Dictionary<int, Cell> ToVisit = new Dictionary<int, Cell>();
            foreach (var item in Map)
            {
                if (item.Value.isOpen)
                {
                    ToVisit.Add(item.Key, item.Value);
                    Keys.Add(item.Key);
                }
            }

            Random rndKey = new Random();
            int key = Keys[rndKey.Next(1, Keys.Count - 1)];
            DFS(bufPathdfs, idEnter, ToVisit, key);

            //List<Cell> newPath = new List<Cell>();
            //int idcellAvatar = key;
            //while (true)
            //{
            //    newPath = newPath.Append(Map[idcellAvatar]).ToList();
            //    if (idcellAvatar == idEnter)
            //        break;
            //    idcellAvatar = Map[idcellAvatar].vmin;
            //}
            //newPath.Reverse();
            //bufPathdfs = newPath;

            Console.WriteLine($"DFS закончил свою работу ключ: {key}");

            //A*
            List<Cell> buf = A(key, idExit);

            Console.WriteLine($"A* закончил свою работу ключ: {key}");

            List<int> pathid = new List<int>();
            for (int i = 0; i < buf.Count; i++)
                pathid = pathid.Append(buf[i].id).ToList();

            #region Очистка Map
            foreach (var item in Map)
                if (item.Value.Passed)
                    Map[item.Key].Passed = false;
            #endregion
            #region отобразить путь в лабиринте
            Map[ToVisit[key].id].isKey = true;
            for (int i = 0; i < pathid.Count; i++)
                Map[pathid[i]].Passed = true;

            for (int i = 0; i < bufPathdfs.Count; i++)
                Map[bufPathdfs[i].id].PassedDFS = true;
            #endregion
            Write();
            Console.WriteLine("программа закончила работу");
            Console.ReadLine();
        }
    }
}
