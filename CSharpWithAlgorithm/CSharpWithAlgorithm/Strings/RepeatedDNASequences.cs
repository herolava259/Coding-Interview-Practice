using System.Text;


namespace CSharpWithAlgorithm.Strings;

public static class RepeatedDNASequencesSolution
{
    public static IList<string> FindRepeatedDnaSequences(string s)
    {
        int encode(string s)
        {
            return s.Aggregate(0, (res, c) =>
            {
                res <<= 2;
                res |= c switch
                {
                    'A' => 0,
                    'C' => 1,
                    'G' => 2,
                    'T' => 3,
                    _ => throw new ArgumentException("Invalid character!!!")
                };

                return res;
            });
        }

        string decode(int bits)
        {
            var sb = new StringBuilder();

            for(int i =0; i < 10; ++i)
            {
                var enc = bits & 3;

                var nuc = enc switch
                {
                    0 => 'A',
                    1 => 'C',
                    2 => 'G',
                    3 => 'T',
                    _ => 'A'
                };

                sb.Insert(0, nuc);

                bits >>= 2;
            }

            return sb.ToString();
        }

        int shift(int bits, char nuc)
        {

            bits <<= 2;
            bits &= ~(3 << 20);
            return bits | nuc switch
            {
                'A' => 0,
                'C' => 1,
                'G' => 2,
                'T' => 3,
                _ => throw new ArgumentException("Invalid nuc arg!!!")
            };
        }

        if (s.Length < 10)
            return [];

        var curBitsWindow = encode(s.Substring(0, 10));

        var seen = new HashSet<int>();
        var repeated = new HashSet<int>();

        seen.Add(curBitsWindow);

        for(int i =10; i < s.Length; ++i)
        {
            curBitsWindow = shift(curBitsWindow, s[i]);

            if(!seen.Add(curBitsWindow))
                repeated.Add(curBitsWindow);
        }

        return repeated.Select(c => decode(c)).ToList();
    }
}
