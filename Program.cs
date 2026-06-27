using System;

namespace Домашнее_задание_урока_8__1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double number1, number2, result; // Объявление числовых переменных

            string msg; // Объявление строковой переменной

            Console.WriteLine("Введите число 1");

            msg = Console.ReadLine(); // Ожидание ввода в консоль числа 1

            number1 = double.Parse(msg); // Преобразование строки в число

            Console.WriteLine("Введите число 2");

            msg = Console.ReadLine(); // Ожидание ввода в консоль числа 2

            number2 = double.Parse(msg); // Преобразование строки в число

            result = (number1 + number2) / 2; // Вычисление среднего арифметического

            Console.WriteLine("Среднее арифметическое равно: " + result);
        }
    }
}
