# Parcel

Forensics<br/>
176 solves, 200 pts<br/>

### Description
That's a lot of magick<br/>
~knif3<br/>
[File](./Assets/Parcel/Parcel_original)

<br/><br/><br/>

### Solution
We extract the gzip file to obtain this [file](./Assets/Parcel/Parcel)<br/>
We notice a lot of base 64 encoded images in the file<br/>
Hence, we copied and converted the larger chunks of base 64 encoded images<br/>
We realise that it is a bunch of pieces to an image of a string<br/>
Hence, we reassemble it with what we have, using Medibang Paint Pro<br/><br/>
<img src="./Assets/Parcel/Parcel_Constructed.png" width="50%" height="50%"><br/>
<br/>
> RS{Im_doing_a_v1rtual_puzzl3}