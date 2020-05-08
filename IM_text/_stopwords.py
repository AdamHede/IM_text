# This list of English stop words is taken from the "Glasgow Information
# Retrieval Group". The original list can be found at
# http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
ENGLISH_STOP_WORDS = frozenset([
    "a", "about", "above", "across", "after", "afterwards", "again", "against",
    "all", "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
    "around", "as", "at", "back", "be", "became", "because", "become",
    "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
    "below", "beside", "besides", "between", "beyond", "bill", "both",
    "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
    "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
    "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
    "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
    "find", "fire", "first", "five", "for", "former", "formerly", "forty",
    "found", "four", "from", "front", "full", "further", "get", "give", "go",
    "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
    "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
    "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
    "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
    "latterly", "least", "less", "ltd", "made", "many", "may", "me",
    "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
    "move", "much", "must", "my", "myself", "name", "namely", "neither",
    "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
    "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
    "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
    "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "same", "see", "seem", "seemed",
    "seeming", "seems", "serious", "several", "she", "should", "show", "side",
    "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
    "something", "sometime", "sometimes", "somewhere", "still", "such",
    "system", "take", "ten", "than", "that", "the", "their", "them",
    "themselves", "then", "thence", "there", "thereafter", "thereby",
    "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
    "third", "this", "those", "though", "three", "through", "throughout",
    "thru", "thus", "to", "together", "too", "top", "toward", "towards",
    "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
    "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
    "whence", "whenever", "where", "whereafter", "whereas", "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
    "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself",
    "yourselves"])

DANISH_STOP_WORDS = frozenset(['ad',
 'af',
 'aldrig',
 'alene',
 'alle',
 'allerede',
 'alligevel',
 'alt',
 'altid',
 'anden',
 'andet',
 'andre',
 'at',
 'bag',
 'bare',
 'begge',
 'bl.a.',
 'blandt',
 'blev',
 'blive',
 'bliver',
 'burde',
 'bør',
 'ca.',
 'da',
 'de',
 'dem',
 'den',
 'denne',
 'dens',
 'der',
 'derefter',
 'deres',
 'derfor',
 'derfra',
 'deri',
 'dermed',
 'derpå',
 'derved',
 'det',
 'dette',
 'dig',
 'din',
 'dine',
 'disse',
 'dit',
 'dog',
 'du',
 'efter',
 'egen',
 'ej',
 'eller',
 'ellers',
 'en',
 'end',
 'endnu',
 'ene',
 'eneste',
 'enhver',
 'ens',
 'enten',
 'er',
 'et',
 'f.eks.',
 'far',
 'fem',
 'fik',
 'fire',
 'flere',
 'flest',
 'fleste',
 'for',
 'foran',
 'fordi',
 'forrige',
 'fra',
 'fx',
 'få',
 'får',
 'før',
 'først',
 'gennem',
 'gjorde',
 'gjort',
 'god',
 'godt',
 'gør',
 'gøre',
 'gørende',
 'ham',
 'han',
 'hans',
 'har',
 'havde',
 'have',
 'hej',
 'hel',
 'heller',
 'helt',
 'hen',
 'hende',
 'hendes',
 'henover',
 'her',
 'herefter',
 'heri',
 'hermed',
 'herpå',
 'hos',
 'hun',
 'hvad',
 'hvem',
 'hver',
 'hvilke',
 'hvilken',
 'hvilkes',
 'hvis',
 'hvor',
 'hvordan',
 'hvorefter',
 'hvorfor',
 'hvorfra',
 'hvorhen',
 'hvori',
 'hvorimod',
 'hvornår',
 'hvorved',
 'i',
 'igen',
 'igennem',
 'ikke',
 'imellem',
 'imens',
 'imod',
 'ind',
 'indtil',
 'ingen',
 'intet',
 'ja',
 'jeg',
 'jer',
 'jeres',
 'jo',
 'kan',
 'kom',
 'komme',
 'kommer',
 'kun',
 'kunne',
 'lad',
 'langs',
 'lav',
 'lave',
 'lavet',
 'lidt',
 'lige',
 'ligesom',
 'lille',
 'længere',
 'man',
 'mand',
 'mange',
 'med',
 'meget',
 'mellem',
 'men',
 'mens',
 'mere',
 'mest',
 'mig',
 'min',
 'mindre',
 'mindst',
 'mine',
 'mit',
 'mod',
 'må',
 'måske',
 'ned',
 'nej',
 'nemlig',
 'ni',
 'nogen',
 'nogensinde',
 'noget',
 'nogle',
 'nok',
 'nu',
 'ny',
 'nyt',
 'når',
 'nær',
 'næste',
 'næsten',
 'og',
 'også',
 'okay',
 'om',
 'omkring',
 'op',
 'os',
 'otte',
 'over',
 'overalt',
 'pga.',
 'på',
 'samme',
 'sammen',
 'se',
 'seks',
 'selv',
 'selvom',
 'senere',
 'ser',
 'ses',
 'siden',
 'sig',
 'sige',
 'sin',
 'sine',
 'sit',
 'skal',
 'skulle',
 'som',
 'stadig',
 'stor',
 'store',
 'synes',
 'syntes',
 'syv',
 'så',
 'sådan',
 'således',
 'tag',
 'tage',
 'temmelig',
 'thi',
 'ti',
 'tidligere',
 'til',
 'tilbage',
 'tit',
 'to',
 'tre',
 'ud',
 'uden',
 'udover',
 'under',
 'undtagen',
 'var',
 'ved',
 'vi',
 'via',
 'vil',
 'ville',
 'vor',
 'vore',
 'vores',
 'vær',
 'være',
 'været',
 'øvrigt'])