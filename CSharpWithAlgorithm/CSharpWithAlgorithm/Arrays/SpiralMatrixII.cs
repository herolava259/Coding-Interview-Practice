
namespace CSharpWithAlgorithm.Arrays;

public static class SpiralMatrixII
{
    public static int[][] GenerateMatrix(int n)
    {
        var result = Enumerable.Range(0, n).Select(_ => Enumerable.Repeat(0, n).ToArray()).ToArray();

        (int, int, int, int, int) changeStateX(int state, int first, int last)
        {
            return state switch
            {
                0 => (1, 0, first, last, last),
                1 => (2, -1, first, Math.Max(last - 1, first), Math.Max(last - 1, first)),
                2 => (3, 0, first, last, first),
                3 => (0, 1, Math.Min(first + 1, last), last, Math.Min(first + 1, last)),
                _ => (0, 1, Math.Min(first + 1, last), last, Math.Min(first + 1, last)),
            };
        }

        (int, int, int, int, int) changeStateY(int state, int first, int last)
        {
            return state switch
            {
                0 => (1, 1, Math.Min(first + 1, last), last, Math.Min(first + 1, last)),
                1 => (2, 0, first, last, last),
                2 => (3, -1, first, Math.Max(first, last - 1), Math.Max(first, last - 1)),
                3 => (0, 0, first, last, first),
                _ => (0, 0, first, last, first),
            };
        }

        bool endStateX(int pointer, int first, int last, int state)
        {
            return state switch
            {
                0 => pointer > last,
                1 => false,
                2 => pointer < first,
                3 => false,
                _ => false
            };
        }

        bool endStateY(int pointer, int first, int last, int state)
        {
            return state switch
            {
                0 => false,
                1 => pointer > last,
                2 => false,
                3 => pointer < first,
                _ => false
            };
        }



        var (stateX, deltaX, firstX, lastX, pointerX) = changeStateX(-1, -1, n - 1);
        var (stateY, deltaY, firstY, lastY, pointerY) = changeStateY(-1, 0, n - 1);

        for (int counter = 1; counter <= n * n; ++counter)
        {
            if (endStateX(pointerX, firstX, lastX, stateX) || endStateY(pointerY, firstY, lastY, stateY))
            {
                (stateX, deltaX, firstX, lastX, pointerX) = changeStateX(stateX, firstX, lastX);
                (stateY, deltaY, firstY, lastY, pointerY) = changeStateY(stateY, firstY, lastY);
            }

            result[pointerY][pointerX] = counter;

            pointerX += deltaX;
            pointerY += deltaY;

        }

        return result;
    }
}
