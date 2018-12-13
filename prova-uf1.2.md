# Prova M02 - UF1.2 - 13/12/2018
## IES ESCOLA DEL TREBALL BARCELONA

### COGNOMS:_______Singh Kaur_____________________ NOM:__Amanjot_________________

### CURS:_________1JISM______________

PUNTUACIÓ: Totes les preguntes valen 1 punt i per tant podríeu obtenir 11 punts. 

**1. Feu la descàrrega de la imatge de debian (des de mirror: debian-9.5.0-amd64-netinst.iso) des de línia d'ordres. Poseu aquí la comanda i l'estat del procés:**
debian-9.5.0-amd64-netinst.iso
	- Ordre per descarregar desde línia d'ordres: mount -o loop `debian-9.5.0-amd64-netinst.iso /mnt/debian/
	- Ordre per veure l'estat del procés mentre es descarrega, sortida per pantalla i estat en el que es troba: top o htop

**2. Poseu el procés de descàrrega (si cal inicieu-la de nou) en estat aturat. Mostreu l'estat del procés de descàrrega:**

	- Ordre per posar-la en estat aturat: Ctrl+ z
	- Ordre i sortida de l'ordre per veure'n l'estat: watch ls -lh.

**3. Com podem retornar el procés a primer plà?**

    - Indiqueu com ho heu fet i copieu el resultat de la l´inia d'ordres: Amb la comanda fg(foreground)
[guest@g23 ~]# fg
watch ls -lh

[1]+  Stopped                 watch ls -lh
**4. Creeu al directori que vulgueu un disc (de nom el que vulgueu) on instal.lar el debian server. El disc ha de tenir format qcow2 i ser de 11G incrementals**
	
	- Ordre per crear-lo: qemu-img create -f qcow2 ./debian.qcow2 11G

	- Ordre i sortida de l'ordre per veure la informació del disc creat: qemu-img info debian.qcow2
	image: debian.qcow2
	file format: qcow2
	virtual size: 11G (11811160064 bytes)
	disk size: 196K
	cluster_size: 65536
	Format specific information:
          compat: 1.1
    	  lazy refcounts: false
    	  refcount bits: 16
    	  corrupt: false
   ** Creeu un segon disc per a dades incremental de 10MB. Aquest disc s'ha d'anomenar dades.qcow2.** 
    
    - Ordre per crear-lo: qemu-img create -f qcow2 ./dades.qcow2 10G

**5. Creeu ara una màquina virtual (no la arrenqueu encara) amb les opcions per defecte per instal.lar el debian server i el disc que heu creat abans.**
    **Poseu-li de nom el número 1 i el vostre nom separat per guions baixos amb extenxió xml  (p.ex. 1_josep_maria_vinolas_auquer.xml)**
    **Una vegada creada volqueu-ne la descripció en format XML en un fitxer amb el mateix nom (sense extensió)**
    
    - Entregueu-lo al moodle com a part de la prova.
	- Ordre que heu fet servir per generar el fitxer XML: virsh dumpxml 1_amanjot_singh_kaur.xml

**6. Modifiqueu la màquina virtual per tal que tingui:**

	Memòria RAM: 800MB
	Nombre de fils de processador: 2
	Interfície de xarxa: Conectada directament a l'interficie física
	Afegiu el segon disc dur de 2MB amb interfície IDE per a dades

   **Poseu-li de nom el número 2 i el vostre nom separat per guions baixos  (p.ex. 2_josep_maria_vinolas_auquer.xml)**
   **Una vegada creada envieu-ne la descripció en format XML en un fitxer amb el mateix nom i amb extenxió xml.**
   
   - Entregueu-lo al moodle com a part de la prova.
   - Ordre que heu fet servir per generar el fitxer XML: virsh dumpxml 2_amanjot_singh_kaur.xml
   
   
**7. Inicieu ara la instal.lació del debian i instal.leu-lo al disc dur de 11G amb opcions per defecte.**
** Inicieu l'instal.lació simple (no gràfica) i a la pantalla de selecció de programari selecvioneu només la última opció de 'standard system utilities'**
** Mentre s'instal.la mostreu l'estat del procés que està virtualitzant el maquinari per a aquesta màquina virtual**
   
	- Ordre i sortida de l'ordre per pantalla que ens permet veure l'estat d'aquest procés. Amb la comanda ps o watch.

**8. Mentre s'instal.la poseu-la des de línia d'ordres en pausa i reinicieu-la posteriorment.**

	- Ordre per pausar-la: virsh suspend debian
	- Ordre per veure'n l'estat i sortida d'aquesta ordre: virsh list
	- Ordre per reanudar-la: virsh resume debian
	- Ordre per veure la URI del visor i sortida d'aquesta ordre: virsh domdisplay debian

**9. Una vegada instal.lat el debian server (i sense apagar-lo) afegiu-hi una interfície de xarxa, model virtio, de tipus NAT i mostreu-ne la direcció IP.**

	- Ordre i sortida per a visualitzar les adreces IP del servidor: ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:4d:78:5e brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.104/24 brd 192.168.122.255 scope global dynamic ens3
       valid_lft 3343sec preferred_lft 3343sec
    inet6 fe80::c8de:6068:27dc:f8ad/64 scope link 
       valid_lft forever preferred_lft forever
3: ens11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:0b:2c:14 brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.220/16 brd 192.168.255.255 scope global dynamic ens11
       valid_lft 21493sec preferred_lft 21493sec
    inet6 fe80::3028:81a:abc6:cbae/64 scope link 
       valid_lft forever preferred_lft forever
	
**10. Una vegada instal.lada inicialitzeu el disc de 10M incremental que heu creat**

	- Indiqueu quina ordre i la sortida heu fet servir per a identificar el disc en el vostre sistema: lsblk
	- Creeu-hi un sistema de fitxers EXT4 i indiqueu-ne l'ordre per a fer-ho: fdisk /dev/sda
	- Munteu aquest disc al directori /mnt amb l'ordre mount. Si cal mireu el manual i indiqueu l'ordre:
mount -o loop `debian.qcow2 /mnt/debian/

**11. Ara redirigiu la sortida de l'ordre que mostra les adreces IP del servidor a un fitxer anomenat adreces.out dins el directori /mnt on teniu muntat el disc de 10M.**
	
	- Ordre per crear el fitxer amb la sortida de les adreces IP: .adreces.out & jobs
	- Apagueu la màquina i pugeu a l'entrega del moodle aquest disc dades.qcow2.
	
## Recordeu a entregar finalment al moodle també la prova amb les respostes!

