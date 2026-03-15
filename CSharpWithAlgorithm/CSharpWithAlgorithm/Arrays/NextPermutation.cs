using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Arrays;

public static class NextPermutation
{
    public static int[] Solve(int[] nums)
    {
        int findMinimalSupremePosition(IList<int> sequence, int begin, int end, int val)
        {
            // precondition:
            // ensure that elements have position in range from begin to end is non-increase array
            // and val always less than element at begin position of sequence
            // begin <= end

            var pointer = begin;

            while (pointer <= end && sequence[pointer] > val) pointer++;

            return Math.Max(pointer - 1, begin);
        }



        int lowerBoundPositionOfNonIncreaseSubSequence(IList<int> sequence)
        {
            int pointer = sequence.Count - 1;

            while (pointer > 0 && sequence[pointer - 1] >= sequence[pointer])
                --pointer;

            return pointer - 1;
        }

        void swap(IList<int> sequence, int positionOne, int positionTwo)
        {
            // 1 ^ 1 = 0
            // 0 ^ 1 = 1
            // 1 ^ 0 = 1
            // 0 ^ 0 = 0
            // 0 ^ 1 = (1 ^ 0) ^ 0 = 1
            // => a ^ b ^ a = b
            // => b ^ a ^ b = a
            sequence[positionOne] ^= sequence[positionTwo]; // the left side contain info of both
            sequence[positionTwo] ^= sequence[positionOne]; // now the left side of the assigment contain only element-one (property of xor operation)
            sequence[positionOne] ^= sequence[positionTwo]; // xor assignment again the left side contain only info of  element-two
        }

        void internalReverse(IList<int> sequence, int begin, int end = -1)
        {
            // precondition before calling the function:
            // begin <= end
            // begin >= 0
            // end < len-of-sequence
            if (end == -1)
                end = sequence.Count - 1;

            while (begin < end) swap(sequence, begin++, end--);

        }

        IList<int> nextPermutation(IList<int> sequence)
        {
            var nextSequence = sequence.ToList();
            // ensure that lowerBoundIdx always greater than or equal 0 when calling the function.
            var lowerBoundIdx = lowerBoundPositionOfNonIncreaseSubSequence(nextSequence);
            var subsIdx = findMinimalSupremePosition(nextSequence, lowerBoundIdx + 1, nextSequence.Count - 1, nextSequence[lowerBoundIdx]);
            swap(nextSequence, lowerBoundIdx, subsIdx);
            internalReverse(nextSequence, lowerBoundIdx + 1, nextSequence.Count - 1);
            return nextSequence;
        }

        return nextPermutation(nums).ToArray();
    }
}
