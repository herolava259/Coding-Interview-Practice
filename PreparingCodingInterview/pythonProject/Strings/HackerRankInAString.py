import os
import sys
import re
from collections import defaultdict


def hackerrankInString(s):
    pattern = 'hackerrank'

    dp = defaultdict(lambda: -1)

    first_id_h = 0

    while(first_id_h < len(s) and s[first_id_h] != 'h'):
        first_id_h += 1
    if first_id_h == len(s):
        return 'NO'

    dp['h'] = first_id_h

    curr_prefix = 'h'
    counter = 1
    for i in range(first_id_h + 1, len(s)):
        if counter == len(pattern):
            break
        if pattern[counter] == s[i]:
            curr_prefix += pattern[counter]
            counter += 1
            dp[curr_prefix] = i


    if dp[pattern] == -1:
        return 'NO'
    else:
        print(dp)
        return 'YES'


input = 'eynakewdemmmckzsucgxoqeqycdtaldqtfiqvwtkmokfcjzagmdnvkggvfyyskilopsxsfabkmkndkjuboussoitveeybtkbixnclzftkxmafugelqfjyqpjgpnbaupbwtxppmysttxswpsqqgakbftwzdmbtongvplioblkmlacjpnqkiusbjcjjgfxlgtvcbkfboouszbnoyscywdbwacxgpixbsinaexfntstzlgdtmwfztoixqcoznkcmxaelawlqwyemqactkinvvsslpfbanbfiulkveaxiywoqezoagagfksteomjajoeoendamddcxspdngqplmlsodpjdpxvxquyikpqxwjafviuzcgfqcnnqwcvgjsvoxypzeklfwwzbwnqtucijzkiicdfiavixcnxklcwgwtnsdabkgyaxjvffqstocslengoszfmlmptbafcmcfddzoyilvvbdymecyyvjwsmaykbwvyssykotmpgmlfombabpqggmiatyzzvbycxpekxvbnoxdvwnjieaiykkggomefesqwzqnmvquuxtexuzgeaxiwjfcyouwyswbcgskjzsvstvjlyizptszdtzsetfsidmgvaukpizuobgqiulzoxeduoiqojpzsauplcyuyvwlwlvcawgwukjudswmazemubgwgbfesiollpenzzvetyqkjngovtumcltjfzgnlpqjdztywejvzbwltfpnysewdzkiypgoyjflwqvanoplyfeijzimldikzyvsfkylwaapupzwypavilubitvtdjfxyccixyanlejpmtizpnnouyyixegpepwvuimfiknmkwofutgcnustcayttgsptlduwatiuvypfczqxnyvlwkuvxnjsjduxyqwmfqxvbkxlqnkplyjnzlccqoivwtlzatymodsgwgwwnemfulfwbpokgxtfasbjwcusxjtqqzyeyoqwlmfaotgpxlweqymqgyqajlywlggxabsmfyebkfiswyxbausggtwevydznadupdxkuxayoyxadcnqigfjftmggkqgzvzdlmblebvqmfytpucxwmzfuqsfgqatzaixfsdymnilifnalnlvfoldavyvckdlpcladqwkmwmukbqztegcxctjvcseusvenlwwlxwwjnbwoqsyeqvcjwxmypyawqtyeqzeugnwzlljxtvkcjmdjmgqxqxcxinlilulsjvkqinlcyktjzvdvpnwpzytqjzugwpfxwxlqpkqsdftedqljmgxvjldbsjavgwnagtsgusoqcfucatagxtmkwnucvmbmfkgkvocjavggtkvmsgdlojzelqqmveejiyljxkeatkylmpdmkkbeeczqdagocbkpaxmnwydnxftxdxscydxakvlysdxntjnfobukdmqptoxwqezwstzppwxculyjxaxeiddjpyjvnvsgjyeawcujuatpqvfuywumafddywitkxgsnnwayvfzxafwjoetqymzlycbcmnulmbslzlgtvjvstfjnkgtbzdltayazlqnzdueasxwjuaxtvgzvdjsmunisdynbsqzeetyoxjskpuziuioqbptdywzwlstqawvkbzxppmspobkumobkdsflgkqplnzzpcneuwxmwcwdqkxineiseipxtcfzqmulbycgzecvdjqynwvwwnzmbyxgzcnwobymoxqtakziaizxbauqmcmgovjnugmozqmampnwpuikgoxlgciyjoizvkqaqfsombwgwamvbdvsuoekffgetoktuedqyggqsastzxpmpwjxgeojktdjvputndyxdfvuavgojpwywvcbeazczumfixdbqtlqmqgwuzxzeiabmekmdomuoqvlmwifqctknniydpjzgitcqmqxxswnlndkjavpikaylqdypuwlmxozcxazmatpytbqlntyecipmkinppulzqqoefatiwovvbwdyayjdypkjiesqupwxcufpdfuukzpqqqylywposxxpwqudzezetkgbugvwvkktvkjdmjdtsiyksjaecxcloyngbozajbyoefobiyxxfdnlcakqqtquyfileomxxinaogtbxdldyfetdiuduiylnqvzzsygsxapuvwppaodqvdkfjtdljffwbfxbaytpfpflqffsakgayexqfgailsuenfemuokbytkiqlxpomcvuqjcpuzgqcmkiszgwnkgavxnfzndybmxogjaqoazljcfylgzacqjwxfmjfbnoebxbtvnbfyqswmjsvobpnwkixlqoficvpntjliqgmptwppttqswpdosduqydzbtzqspbqgezneaszivyifmwmjocbdqimdfabpqlyoxsmwxmmakyvkslspobylnbikcwfqgvkegzlfwbuqxevdtnnszaneyztnxctmzigbmuskbpnxidcfalxefyuubybjtyvglsypbmwwdjfoombfovuldsmtebjzqjyccufwnfwnudubusalqmqmovdavwuaitdtjqdyisbswmupvqjlwlkupbuvkwjegctxpueefbtkuiwixqnnivqbodtzvcznydqcpsxjlqocdqyiswyxyvxmnqjwvxijzukxjjwmnsxpktwumldndbldippkdwpaikozextncofneugebkxbspmewbumbagzpscfvczfisncguzffapcfvjoqfvwjewmqgppoxievmmxaeeexuxffupxejotwgegliwaewozkqdmnplyltfzgeikxzgipdqywktqaaijvmtfilumuijnuidxwkgouxulcljguibcdxxvgxonccktlqvpownbltzgenskjvnltsdjmbxsfcexocqcenamvqbqfqootiobcllwxwkoovsgvlvuaolozaltmcmcbsacjpsdsfuuapccfozdbnjavcnscdjxtyfjumceiuuoxsfylsjtdtltystdicpcslvmzjobjmvtueevtytddsfiauuvuiyxnundjfidvzzmacqveiznavoiupsivqimlkvggoqgcpfyttwtiievcafwlvcatcoscdvgobcgqkoufxucpwbkcguabfyvpmnsaznjueeocsnuxpqaujqpvsiaszquptmgtjxkcvqnclynnpxvjxgzepfkngwxipexwybolnpufzqleczzsdeoffxvxwimyfptqdecgknuegyswxvszmanicgtqxbajqkgzndjvayvqyusomlebyquipfeuugvdycmiczlqmsxboqodonpmynfcwllgijqeupqelxiyvzxayazyawojzowxskpxceupoxwfagdjyjddtjsqzaollppctyotaiuneizwiqkdawdyfsbevgfmumbakuxeyvfcfmtxnbcpuwstxwzxllknwaincqtcdzbxyanccdglauskwgpyblutslzsuummxnkzyloqddzcsesoxgmynwcpiiqmtniaovmfwbdgppkxsdaivguteaaekugiuugcqzqjvyskvooncvctpwmtjnegkctlfaakepfwkdoswxpodsammklaoatpmwydcmiacslxmxodjtulfvxyvvgbapmwkcoyezptplqvzjaeplytjnkiicecxeittzekadsbosmznzlvasgnquvmotaencnjxommjknzlwbxwvmjwaojscwtzebfsynlpvkvfiwxpdxteepnoljeaxgdvwnnywpbimauqbffzqavibtkusybiisoejgxddvignqppxdywpkyujlemmjogsxasqkquiwcqgepgjivwoiddlvnubfjzqtukivvzpsclyzxuwjzcguuafmezztmwuxzmbzxfpggjteqjunteygxgsuasgduualsekiasipscleglyosandtyoioazxfyuwpwputukpcvwajqpilcomgowmmuqcelocqgvyignwfgidnpxswbjjcdsosbtbnevoimisuwxysfmgjzxysjtczxxckdapoqbjbbmtwazmvsdjpkjkaxzyninkjqvealioeiwafsbfkyednweoweypckpvigfapwavftvnstjzxufyxceiwkbpifdosktwsyoqjuegwqgwwyasfppkzymlikpxwmwsmouumynvknbdueboupuxyllunditknvnfejcgmyvmzlzqjzypnjzkibpvvmfbgtdccxcnxiipcfbjbcemlcxaxfpyqkuoepkdxtmbnivuebqslvejfozsivxynvgjuzfjmbnleudmiqjdonwjtzeevgoudxkzkyeimbbtlxsayblofwfbebamssngpxklvxjdzxvpvspgzdinulpvnflbjctufvwnzofvkpduvfyupuywbvnmeudqvvdbdydxbivbvmvlfpwkeamtjvxcvdtpjgfbumavmnbojeepvmjoxopdlkcpzkxlitpcdaqsjpolawzqbxozlpntwyieuydttvnbgxmtzopiflpxpxdljqlgzbpbnjjdbafupvtzlqygdggsufvcpvisslfyvcqxcnfwtokibxndiyacvnwqxwfufnviocmcspbfeqjqppziajjvaqmegwjujcjswwivakzbcgtnnjazpntejiefmdovdblwbylkbeevbcspnspcifnzqglsjtxylwkpglclsjgauzcxqtpgvabclpkyaifdnczxkywjqefyiwmdmjbcuifztlzzzitesqvlekpmjudnmcjakvbtmpxnnzybzpazcvcjinoqckwvzkynycocdwavfndnkfnofdlejnfckluiukfpgwojjdxkxezvqvlmqfjgvxgxekslnpnwdqdlbdbxzwgqumzbxzefuvisuumxjcvafbondmtzqapaqjaulzjsepsfzxmpnjsdenxtiuppzaydtuzfmqqecxzxwnklgeknppytwvlxzjdcwwcoobbiljnsyobeiudozbulvvcsotljfmjfuzacinnggqfidgflbablkwvayxudobjzxyiiqtxwfypmndwbttxuccvtmqbsyaqmyjcqjufewceutybcxnowfjzymsvowkifbuydjpwibtbmwojqzqqkgnecglxzoidbvbvvciowtztbeutdndmwdgbcfppqiydoaplyfbjunqqdubutysgvddismodotqbkwpkigmddnzqsaddulbxzwqixtjljcailydkxbfquvynpdztkmxdzoilmazvudpnlijqxfvpbqpslnqztdmtdtjfxzpxeoaunswsucazekdaoenbxxljizfseeftuwonpaseidlafukobtmzowowxdkqnzjwnkjamxwwecmwgqqmaovamgczybxbedsulkqbjwbfiyektilzvkigjvmyqatzocvmindtkvlnjgjfqwexzecuafkfktfytgkeylvtwkvivsxueqnznliatwwgltvzgkbpwbbgsyxzkdipcielgkjlcaffsxkeybuqtzsjeuupxcvuuvsoftjgdzmgdvsvzoqjontwwdcnwgvatkaiyokzcaiylbdnewwdxmaiqoxtltsaexgivjofwafpni'

print(hackerrankInString(input))