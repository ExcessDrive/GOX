#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, switches first...
        Ependes = self.addSwitch( 's0' )
        Olten = self.addSwitch( 's1' )
        Souppes = self.addSwitch( 's2' )
        Briare = self.addSwitch( 's3' )
        Nevers = self.addSwitch( 's4' )
        Bourbon = self.addSwitch( 's5' )
        Charolles = self.addSwitch( 's6' )
        Belleville = self.addSwitch( 's7' )
        SaultBrenaz = self.addSwitch( 's8' )
        Lavours = self.addSwitch( 's9' )
        Lyon = self.addSwitch( 's10' )
        Unknown = self.addSwitch( 's11' )
        Montfaucon = self.addSwitch( 's12' )
        Antwerp1 = self.addSwitch( 's13' )
        Toulouse = self.addSwitch( 's14' )
        BrusselsMIDI = self.addSwitch( 's15' )
        Marseille = self.addSwitch( 's16' )
        Bordeaux = self.addSwitch( 's17' )
        AzySurMarne = self.addSwitch( 's18' )
        Meaux = self.addSwitch( 's19' )
        Revigny = self.addSwitch( 's20' )
        CondeSurMarne = self.addSwitch( 's21' )
        Leers = self.addSwitch( 's22' )
        Antoing = self.addSwitch( 's23' )
        Thourotte = self.addSwitch( 's24' )
        Courrieres = self.addSwitch( 's25' )
        Gent = self.addSwitch( 's26' )
        Antwerp2 = self.addSwitch( 's27' )
        Bern = self.addSwitch( 's28' )
        Zurich = self.addSwitch( 's29' )
        Basel = self.addSwitch( 's30' )
        Nancy = self.addSwitch( 's31' )
        Strasbourg = self.addSwitch( 's32' )
        Mannheim = self.addSwitch( 's33' )
        Frankfurt = self.addSwitch( 's34' )
        Internexion = self.addSwitch( 's35' )
        ParisLaDefense = self.addSwitch( 's36' )
        Geneva = self.addSwitch( 's37' )
        Egham = self.addSwitch( 's38' )
        LondonTelehouseNorth = self.addSwitch( 's39' )
        Lowestoft = self.addSwitch( 's40' )
        Amsterdam = self.addSwitch( 's41' )
        Paris = self.addSwitch( 's42' )
        Biaches = self.addSwitch( 's43' )
        Amiens = self.addSwitch( 's44' )
        Crawley = self.addSwitch( 's45' )
        Rotterdam = self.addSwitch( 's46' )
        BrusselsTollaan = self.addSwitch( 's47' )
        Grisolles = self.addSwitch( 's48' )
        BonEncontre = self.addSwitch( 's49' )
        Blois = self.addSwitch( 's50' )
        Nambsheim = self.addSwitch( 's51' )
        Availles = self.addSwitch( 's52' )
        Veretz = self.addSwitch( 's53' )
        Nersac = self.addSwitch( 's54' )
        Blanzay = self.addSwitch( 's55' )
        Meilhan = self.addSwitch( 's56' )
        StChristophe = self.addSwitch( 's57' )
        Andancette = self.addSwitch( 's58' )
        Dusseldorf = self.addSwitch( 's59' )
        Cazan = self.addSwitch( 's60' )
        Montelimar = self.addSwitch( 's61' )
        Pichegu = self.addSwitch( 's62' )
        Fos = self.addSwitch( 's63' )
        Poilhes = self.addSwitch( 's64' )
        Sete = self.addSwitch( 's65' )
        AvigUnknownt = self.addSwitch( 's66' )
        Marseillette = self.addSwitch( 's67' )
        Artenay = self.addSwitch( 's68' )
        StMartin = self.addSwitch( 's69' )
        SnowHill = self.addSwitch( 's70' )
        Pakenham = self.addSwitch( 's71' )
        Zandvoort = self.addSwitch( 's72' )
        Essen = self.addSwitch( 's73' )
        Corbeil = self.addSwitch( 's74' )
        LIsleAdam = self.addSwitch( 's75' )
        Cayeux = self.addSwitch( 's76' )
        Polegate = self.addSwitch( 's77' )
        Xouxange = self.addSwitch( 's78' )
        Troussey = self.addSwitch( 's79' )
        Elten = self.addSwitch( 's80' )
        Leersum = self.addSwitch( 's81' )
        Kapella = self.addSwitch( 's82' )
        Porz = self.addSwitch( 's83' )
        Linz = self.addSwitch( 's84' )
        Dernbach = self.addSwitch( 's85' )
        Naurod = self.addSwitch( 's86' )
        Berg = self.addSwitch( 's87' )

        # ... and now hosts
        Ependes_host = self.addHost( 'h0' )
        Olten_host = self.addHost( 'h1' )
        Souppes_host = self.addHost( 'h2' )
        Briare_host = self.addHost( 'h3' )
        Nevers_host = self.addHost( 'h4' )
        Bourbon_host = self.addHost( 'h5' )
        Charolles_host = self.addHost( 'h6' )
        Belleville_host = self.addHost( 'h7' )
        SaultBrenaz_host = self.addHost( 'h8' )
        Lavours_host = self.addHost( 'h9' )
        Lyon_host = self.addHost( 'h10' )
        Unknown_host = self.addHost( 'h11' )
        Montfaucon_host = self.addHost( 'h12' )
        Antwerp1_host = self.addHost( 'h13' )
        Toulouse_host = self.addHost( 'h14' )
        BrusselsMIDI_host = self.addHost( 'h15' )
        Marseille_host = self.addHost( 'h16' )
        Bordeaux_host = self.addHost( 'h17' )
        AzySurMarne_host = self.addHost( 'h18' )
        Meaux_host = self.addHost( 'h19' )
        Revigny_host = self.addHost( 'h20' )
        CondeSurMarne_host = self.addHost( 'h21' )
        Leers_host = self.addHost( 'h22' )
        Antoing_host = self.addHost( 'h23' )
        Thourotte_host = self.addHost( 'h24' )
        Courrieres_host = self.addHost( 'h25' )
        Gent_host = self.addHost( 'h26' )
        Antwerp2_host = self.addHost( 'h27' )
        Bern_host = self.addHost( 'h28' )
        Zurich_host = self.addHost( 'h29' )
        Basel_host = self.addHost( 'h30' )
        Nancy_host = self.addHost( 'h31' )
        Strasbourg_host = self.addHost( 'h32' )
        Mannheim_host = self.addHost( 'h33' )
        Frankfurt_host = self.addHost( 'h34' )
        Internexion_host = self.addHost( 'h35' )
        ParisLaDefense_host = self.addHost( 'h36' )
        Geneva_host = self.addHost( 'h37' )
        Egham_host = self.addHost( 'h38' )
        LondonTelehouseNorth_host = self.addHost( 'h39' )
        Lowestoft_host = self.addHost( 'h40' )
        Amsterdam_host = self.addHost( 'h41' )
        Paris_host = self.addHost( 'h42' )
        Biaches_host = self.addHost( 'h43' )
        Amiens_host = self.addHost( 'h44' )
        Crawley_host = self.addHost( 'h45' )
        Rotterdam_host = self.addHost( 'h46' )
        BrusselsTollaan_host = self.addHost( 'h47' )
        Grisolles_host = self.addHost( 'h48' )
        BonEncontre_host = self.addHost( 'h49' )
        Blois_host = self.addHost( 'h50' )
        Nambsheim_host = self.addHost( 'h51' )
        Availles_host = self.addHost( 'h52' )
        Veretz_host = self.addHost( 'h53' )
        Nersac_host = self.addHost( 'h54' )
        Blanzay_host = self.addHost( 'h55' )
        Meilhan_host = self.addHost( 'h56' )
        StChristophe_host = self.addHost( 'h57' )
        Andancette_host = self.addHost( 'h58' )
        Dusseldorf_host = self.addHost( 'h59' )
        Cazan_host = self.addHost( 'h60' )
        Montelimar_host = self.addHost( 'h61' )
        Pichegu_host = self.addHost( 'h62' )
        Fos_host = self.addHost( 'h63' )
        Poilhes_host = self.addHost( 'h64' )
        Sete_host = self.addHost( 'h65' )
        AvigUnknownt_host = self.addHost( 'h66' )
        Marseillette_host = self.addHost( 'h67' )
        Artenay_host = self.addHost( 'h68' )
        StMartin_host = self.addHost( 'h69' )
        SnowHill_host = self.addHost( 'h70' )
        Pakenham_host = self.addHost( 'h71' )
        Zandvoort_host = self.addHost( 'h72' )
        Essen_host = self.addHost( 'h73' )
        Corbeil_host = self.addHost( 'h74' )
        LIsleAdam_host = self.addHost( 'h75' )
        Cayeux_host = self.addHost( 'h76' )
        Polegate_host = self.addHost( 'h77' )
        Xouxange_host = self.addHost( 'h78' )
        Troussey_host = self.addHost( 'h79' )
        Elten_host = self.addHost( 'h80' )
        Leersum_host = self.addHost( 'h81' )
        Kapella_host = self.addHost( 'h82' )
        Porz_host = self.addHost( 'h83' )
        Linz_host = self.addHost( 'h84' )
        Dernbach_host = self.addHost( 'h85' )
        Naurod_host = self.addHost( 'h86' )
        Berg_host = self.addHost( 'h87' )

        # add edges between switch and corresponding host
        self.addLink( Ependes , Ependes_host )
        self.addLink( Olten , Olten_host )
        self.addLink( Souppes , Souppes_host )
        self.addLink( Briare , Briare_host )
        self.addLink( Nevers , Nevers_host )
        self.addLink( Bourbon , Bourbon_host )
        self.addLink( Charolles , Charolles_host )
        self.addLink( Belleville , Belleville_host )
        self.addLink( SaultBrenaz , SaultBrenaz_host )
        self.addLink( Lavours , Lavours_host )
        self.addLink( Lyon , Lyon_host )
        self.addLink( Unknown , Unknown_host )
        self.addLink( Montfaucon , Montfaucon_host )
        self.addLink( Antwerp1 , Antwerp1_host )
        self.addLink( Toulouse , Toulouse_host )
        self.addLink( BrusselsMIDI , BrusselsMIDI_host )
        self.addLink( Marseille , Marseille_host )
        self.addLink( Bordeaux , Bordeaux_host )
        self.addLink( AzySurMarne , AzySurMarne_host )
        self.addLink( Meaux , Meaux_host )
        self.addLink( Revigny , Revigny_host )
        self.addLink( CondeSurMarne , CondeSurMarne_host )
        self.addLink( Leers , Leers_host )
        self.addLink( Antoing , Antoing_host )
        self.addLink( Thourotte , Thourotte_host )
        self.addLink( Courrieres , Courrieres_host )
        self.addLink( Gent , Gent_host )
        self.addLink( Antwerp2 , Antwerp2_host )
        self.addLink( Bern , Bern_host )
        self.addLink( Zurich , Zurich_host )
        self.addLink( Basel , Basel_host )
        self.addLink( Nancy , Nancy_host )
        self.addLink( Strasbourg , Strasbourg_host )
        self.addLink( Mannheim , Mannheim_host )
        self.addLink( Frankfurt , Frankfurt_host )
        self.addLink( Internexion , Internexion_host )
        self.addLink( ParisLaDefense , ParisLaDefense_host )
        self.addLink( Geneva , Geneva_host )
        self.addLink( Egham , Egham_host )
        self.addLink( LondonTelehouseNorth , LondonTelehouseNorth_host )
        self.addLink( Lowestoft , Lowestoft_host )
        self.addLink( Amsterdam , Amsterdam_host )
        self.addLink( Paris , Paris_host )
        self.addLink( Biaches , Biaches_host )
        self.addLink( Amiens , Amiens_host )
        self.addLink( Crawley , Crawley_host )
        self.addLink( Rotterdam , Rotterdam_host )
        self.addLink( BrusselsTollaan , BrusselsTollaan_host )
        self.addLink( Grisolles , Grisolles_host )
        self.addLink( BonEncontre , BonEncontre_host )
        self.addLink( Blois , Blois_host )
        self.addLink( Nambsheim , Nambsheim_host )
        self.addLink( Availles , Availles_host )
        self.addLink( Veretz , Veretz_host )
        self.addLink( Nersac , Nersac_host )
        self.addLink( Blanzay , Blanzay_host )
        self.addLink( Meilhan , Meilhan_host )
        self.addLink( StChristophe , StChristophe_host )
        self.addLink( Andancette , Andancette_host )
        self.addLink( Dusseldorf , Dusseldorf_host )
        self.addLink( Cazan , Cazan_host )
        self.addLink( Montelimar , Montelimar_host )
        self.addLink( Pichegu , Pichegu_host )
        self.addLink( Fos , Fos_host )
        self.addLink( Poilhes , Poilhes_host )
        self.addLink( Sete , Sete_host )
        self.addLink( AvigUnknownt , AvigUnknownt_host )
        self.addLink( Marseillette , Marseillette_host )
        self.addLink( Artenay , Artenay_host )
        self.addLink( StMartin , StMartin_host )
        self.addLink( SnowHill , SnowHill_host )
        self.addLink( Pakenham , Pakenham_host )
        self.addLink( Zandvoort , Zandvoort_host )
        self.addLink( Essen , Essen_host )
        self.addLink( Corbeil , Corbeil_host )
        self.addLink( LIsleAdam , LIsleAdam_host )
        self.addLink( Cayeux , Cayeux_host )
        self.addLink( Polegate , Polegate_host )
        self.addLink( Xouxange , Xouxange_host )
        self.addLink( Troussey , Troussey_host )
        self.addLink( Elten , Elten_host )
        self.addLink( Leersum , Leersum_host )
        self.addLink( Kapella , Kapella_host )
        self.addLink( Porz , Porz_host )
        self.addLink( Linz , Linz_host )
        self.addLink( Dernbach , Dernbach_host )
        self.addLink( Naurod , Naurod_host )
        self.addLink( Berg , Berg_host )

        # add edges between switches
        self.addLink( Ependes , Bern, bw=10, delay='0.197072101106ms')
        self.addLink( Ependes , Geneva, bw=10, delay='0.529259387484ms')
        self.addLink( Olten , Bern, bw=10, delay='0.342031132967ms')
        self.addLink( Olten , Zurich, bw=10, delay='0.355214263911ms')
        self.addLink( Souppes , Corbeil, bw=10, delay='0.237449399249ms')
        self.addLink( Souppes , Briare, bw=10, delay='0.310759265752ms')
        self.addLink( Briare , Nevers, bw=10, delay='0.428273828918ms')
        self.addLink( Nevers , Bourbon, bw=10, delay='0.385396309229ms')
        self.addLink( Bourbon , Charolles, bw=10, delay='0.261318598481ms')
        self.addLink( Charolles , Belleville, bw=10, delay='0.25213974161ms')
        self.addLink( Belleville , Unknown, bw=10, delay='0.198611660629ms')
        self.addLink( SaultBrenaz , Lavours, bw=10, delay='0.0597485938392ms')
        self.addLink( SaultBrenaz , Unknown, bw=10, delay='0.0944695616515ms')
        self.addLink( Lavours , Geneva, bw=10, delay='0.241972577798ms')
        self.addLink( Lyon , Andancette, bw=10, delay='0.29186862822ms')
        self.addLink( Lyon , Unknown, bw=10, delay='8.4202521641e-09ms')
        self.addLink( Montfaucon , Cazan, bw=10, delay='0.33824723501ms')
        self.addLink( Montfaucon , Montelimar, bw=10, delay='0.273122653198ms')
        self.addLink( Antwerp1 , Essen, bw=10, delay='0.139377174246ms')
        self.addLink( Antwerp1 , Antwerp2, bw=10, delay='0.0ms')
        self.addLink( Toulouse , Grisolles, bw=10, delay='0.150139312776ms')
        self.addLink( Toulouse , AvigUnknownt, bw=10, delay='0.221363696457ms')
        self.addLink( BrusselsMIDI , BrusselsTollaan, bw=10, delay='0.0ms')
        self.addLink( BrusselsMIDI , Antoing, bw=10, delay='0.480782862987ms')
        self.addLink( Marseille , Cazan, bw=10, delay='0.238520578854ms')
        self.addLink( Marseille , Fos, bw=10, delay='0.215717042395ms')
        self.addLink( Bordeaux , Meilhan, bw=10, delay='0.312227318093ms')
        self.addLink( Bordeaux , StChristophe, bw=10, delay='0.170180965329ms')
        self.addLink( AzySurMarne , Meaux, bw=10, delay='0.0829272015369ms')
        self.addLink( AzySurMarne , CondeSurMarne, bw=10, delay='0.148311721964ms')
        self.addLink( Meaux , Paris, bw=10, delay='0.0795598967595ms')
        self.addLink( Revigny , CondeSurMarne, bw=10, delay='0.156200807322ms')
        self.addLink( Revigny , Troussey, bw=10, delay='0.0761053363005ms')
        self.addLink( Leers , Courrieres, bw=10, delay='0.215390940545ms')
        self.addLink( Leers , Gent, bw=10, delay='0.2977477258ms')
        self.addLink( Leers , Antoing, bw=10, delay='0.123889633586ms')
        self.addLink( Thourotte , Biaches, bw=10, delay='0.249584995744ms')
        self.addLink( Thourotte , LIsleAdam, bw=10, delay='0.286020723791ms')
        self.addLink( Courrieres , Biaches, bw=10, delay='0.301513143926ms')
        self.addLink( Gent , BrusselsTollaan, bw=10, delay='0.295734392658ms')
        self.addLink( Antwerp2 , BrusselsTollaan, bw=10, delay='0.208694177179ms')
        self.addLink( Zurich , Basel, bw=10, delay='0.514625143171ms')
        self.addLink( Basel , Nambsheim, bw=10, delay='0.199077729656ms')
        self.addLink( Nancy , Xouxange, bw=10, delay='0.0087774644083ms')
        self.addLink( Nancy , Troussey, bw=10, delay='0.00916594009102ms')
        self.addLink( Strasbourg , Nambsheim, bw=10, delay='0.378130413558ms')
        self.addLink( Strasbourg , Xouxange, bw=10, delay='0.0651534910762ms')
        self.addLink( Strasbourg , Berg, bw=10, delay='0.172013633716ms')
        self.addLink( Mannheim , Internexion, bw=10, delay='0.370886385768ms')
        self.addLink( Mannheim , Berg, bw=10, delay='0.428766126249ms')
        self.addLink( Frankfurt , Internexion, bw=10, delay='0.0ms')
        self.addLink( Frankfurt , Naurod, bw=10, delay='0.214653510346ms')
        self.addLink( ParisLaDefense , Paris, bw=10, delay='0.0ms')
        self.addLink( ParisLaDefense , LIsleAdam, bw=10, delay='0.144577836738ms')
        self.addLink( Egham , Crawley, bw=10, delay='0.205395288786ms')
        self.addLink( Egham , LondonTelehouseNorth, bw=10, delay='0.103600767361ms')
        self.addLink( LondonTelehouseNorth , SnowHill, bw=10, delay='0.302175719276ms')
        self.addLink( Lowestoft , Zandvoort, bw=10, delay='0.658002219769ms')
        self.addLink( Lowestoft , Pakenham, bw=10, delay='0.284805432427ms')
        self.addLink( Amsterdam , Zandvoort, bw=10, delay='0.102595325528ms')
        self.addLink( Amsterdam , Leersum, bw=10, delay='0.224030213142ms')
        self.addLink( Amsterdam , Rotterdam, bw=10, delay='0.259853324442ms')
        self.addLink( Paris , Corbeil, bw=10, delay='0.142890641504ms')
        self.addLink( Paris , StMartin, bw=10, delay='0.236034822646ms')
        self.addLink( Biaches , Amiens, bw=10, delay='0.325952164208ms')
        self.addLink( Amiens , Cayeux, bw=10, delay='0.469521726846ms')
        self.addLink( Crawley , Polegate, bw=10, delay='0.251301862989ms')
        self.addLink( Rotterdam , Essen, bw=10, delay='0.259796773774ms')
        self.addLink( Grisolles , BonEncontre, bw=10, delay='0.398557013949ms')
        self.addLink( BonEncontre , Meilhan, bw=10, delay='0.388340132593ms')
        self.addLink( Blois , Artenay, bw=10, delay='0.317111281582ms')
        self.addLink( Blois , Veretz, bw=10, delay='0.360398886677ms')
        self.addLink( Availles , Veretz, bw=10, delay='0.490402839425ms')
        self.addLink( Availles , Blanzay, bw=10, delay='0.411152850835ms')
        self.addLink( Nersac , StChristophe, bw=10, delay='0.423341787092ms')
        self.addLink( Nersac , Blanzay, bw=10, delay='0.241487227929ms')
        self.addLink( Andancette , Montelimar, bw=10, delay='0.37701125558ms')
        self.addLink( Dusseldorf , Kapella, bw=10, delay='0.21513830874ms')
        self.addLink( Dusseldorf , Porz, bw=10, delay='0.219083700017ms')
        self.addLink( Pichegu , Sete, bw=10, delay='0.350557562254ms')
        self.addLink( Pichegu , Fos, bw=10, delay='0.283700393914ms')
        self.addLink( Poilhes , Sete, bw=10, delay='0.417875327027ms')
        self.addLink( Poilhes , Marseillette, bw=10, delay='0.233654609457ms')
        self.addLink( AvigUnknownt , Marseillette, bw=10, delay='0.333566968836ms')
        self.addLink( Artenay , StMartin, bw=10, delay='0.333695750949ms')
        self.addLink( SnowHill , Pakenham, bw=10, delay='0.116657907535ms')
        self.addLink( Cayeux , Polegate, bw=10, delay='0.762727165553ms')
        self.addLink( Elten , Leersum, bw=10, delay='0.0869596763099ms')
        self.addLink( Elten , Kapella, bw=10, delay='0.169159843403ms')
        self.addLink( Porz , Linz, bw=10, delay='0.213931313577ms')
        self.addLink( Linz , Dernbach, bw=10, delay='0.171519391622ms')
        self.addLink( Dernbach , Naurod, bw=10, delay='0.456766776387ms')

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = ''

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip=controller_ip, port=6633 ), host=CPULimitedHost, link=TCLink)
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )

    # # DEBUGGING INFO
    # print
    # print "Dumping host connections"
    # dumpNodeConnections(network.hosts)
    # print
    # print "*** Hosts are running sshd at the following addresses:"
    # print
    # for host in network.hosts:
    #     print host.name, host.IP()
    # print
    # print "*** Type 'exit' or control-D to shut down network"
    # print
    # print "*** For testing network connectivity among the hosts, wait a bit for the controller to create all the routes, then do 'pingall' on the mininet console."
    # print

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()


if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork(controller_ip) )
