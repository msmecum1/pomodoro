Console.WriteLine("Hello");

int num1, num2;

Console.Write("Input the first number: ");
num1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input the second number: ");
num2 = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("What do you want to do with those numbers?");
Console.WriteLine("[A]dd");
Console.WriteLine("[S]ubtract");
Console.WriteLine("[M]ultiply");

string operation = Console.ReadLine().ToUpper();

switch (operation)
{
    case "A":
        Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
        break;
    case "S":
        Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
        break;
    case "M":
        Console.WriteLine($"{num1} * {num2} = {num1 * num2}");
        break;
    default:
        Console.WriteLine("Invalid option");
        break;
}

Console.WriteLine("Press any key to close...");
Console.ReadKey();

void PrintFinalEquation(int num1, int num2, int result, string operation)
{

    Console.WriteLine(
        num1 + " " + operation + " " + num2 + " = " + result);
}