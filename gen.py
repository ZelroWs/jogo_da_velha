def gen(jogador):
    j = jogador.lower()
    listam = ('daviddavigabrielarthurlucasmatheuspedroguilhermegustavorafaelfelipebernardoenzonicolasjoão pedropedro henriquecauãvitoreduardodanielhenriquemuriloviniciussamuelpietrovitorleonardocaioheitorlorenzoisaacluccathiagojoão gabrieljoãotheobrunobryancarlos eduardofelipebrenoemanuelryanvitor hugoyuribenjaminerickenzo gabrielfernandojoaquimandrétomásfranciscorodrigoigorantonioianluiz otáviojuanjoão guilhermediogootávionathancalebedaniloluanluiz henriquekaiquealexandrejoão migueliagoricardoraulmarcelojulio césarcauêbeníciovitor gabrielaugustopedro lucasluiz gustavogiovannirenatodiegojoão paulorenanluiz fernandoanthonylucas gabrielthalesluiz miguelhenrymarcos viniciuskevinlevienricojoão lucashugoluiz guilhermematheus henrique')
    listaf = ('ahrihelenaalicelauramanuelasophiaisabellaluísaheloísacecíliamaitêeloáelisalizjúliamaria luísavalentinamaria alicelíviaantonellalorenaaylaisismaria júliamayamaria claraesthergiovannalarasarahbeatrizauroramarianamaria cecíliaolíviamaria helenaisadoralunacatarinamelissamaria eduardalavíniaagathaemanuellymariaalíciarebecaana clarayasminclaramarinaana júliaana luísaisabellyana laurarafaelaana lizstellagabrielavitóriaallanamirellamilenabellaananicoleemillymaria vitóriamariahclariceletícialaísmaria lizbiancamelinajadeana beatrizmaria fernandabetinamaria valentinamaria lauraheloísemaria isiszoelouisemalumelindaana cecíliaana líviaana vitóriamaria heloísachloemaria florpietrapérolaana sophiamaria elisagabriellylarissamaria eloáeduarda')    
    if j in listam:       
        return print(f'Vez do {jogador}')
    elif j in listaf:
        return print(f'Vez da {jogador}')
    else:
        return print(f'Vez de {jogador}')

        

