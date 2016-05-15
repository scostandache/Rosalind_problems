f=open("mass_glossary","r")
mass_table={}
for line in f:
    line=line.split("   ")
    mass_table[line[0]]=line[1].strip("\n")

s="RWYYSPDRWTQCVKKFQSDMGFWWDVCDLNFRHWNESGHLVNSVYHYKHHDNCNMTKLYYAGLSACQYFKRDRYKNSNLTRQSVWRCVNNGIRGSWKMMESDRMTYEFGEIKETWTRHGGNKQHDCETRSEISPCHSHKGNLLGRFSEVMRQKYRHTLGKVEYFEPCTWDPFFWEDYNSPAMEFPVWKQSMMEWILFYVHTRSPHYGESISPGSTVVASTGCPYQDDDNKVCKFICMIHPWHKADDEMDKWWFWSQALKKVEKPYGHCTTSGLAILAWRFPGCQMQLNFHTECWTPDDWICHSDKPSAQICRNEWQYGWDYAHIFLGCSFHQKTYLPMATLESPEWARWRPYVQCKTSCDFTPAGKLAARRWSIRVTAIISTKAAWKCNTSCQKADQVAGMERRILRVNWHVYRYCESCIRQRMWKSCTLRMVMAGFSLPKVAGCKNKTYPFMHQNQCICSCNYKAIIWVECWMLVCVTCHSMFPCNFNLETIRYCCCSSELSVQLMVCHTCDFPSKRSLMKCLMYARMRVVYFGMHGPLDTQYWQPYWLYQDYDVFVSEYVMALPPYRIKLLQCILNNQCTSFGVCKTNLMPNHDFPGRYVYYLSSAPDWWYMQNVHCAKLRVNDPWREITQPANTEWPATDIVMACAQHIDYSAYAPVEEFNMQQVTKMWCKMHQSMVIYFLSPGYLCGSLHWANTCNLCIPESNKWATPHGMWCVIMDVNDQVAKGFTGEPTNAAYVKRQLLCDTEGTMIHMWAVRDAGQCPNHEFAYPKWYSYDVWSACLCVRRLHIEETHLVNLPWIWWPYIKLQDAPQQPQNKQEVEGFARPQVQYMSWHLGM"

mass=0.0
for a in s:
    mass+=float(mass_table[a])
print mass