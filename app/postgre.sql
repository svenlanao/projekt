PGDMP  5    ;                |           projekt    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    projekt    DATABASE     {   CREATE DATABASE projekt WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'German_Germany.1252';
    DROP DATABASE projekt;
                postgres    false            �            1259    16399    autor_buch_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.autor_buch_id_seq
    START WITH 42000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.autor_buch_id_seq;
       public          postgres    false            �            1259    16400    autor_id_seq    SEQUENCE     y   CREATE SEQUENCE public.autor_id_seq
    START WITH 25000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.autor_id_seq;
       public          postgres    false            �            1259    16401    buch_id_seq    SEQUENCE     x   CREATE SEQUENCE public.buch_id_seq
    START WITH 17000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.buch_id_seq;
       public          postgres    false            �            1259    16402 	   tbl_autor    TABLE     �   CREATE TABLE public.tbl_autor (
    autor_id smallint NOT NULL,
    name character varying(30),
    nationalitat character varying(30),
    genre_id smallint
);
    DROP TABLE public.tbl_autor;
       public         heap    postgres    false            �            1259    16405    tbl_autor_buch    TABLE     �   CREATE TABLE public.tbl_autor_buch (
    autor_buch_id integer DEFAULT nextval('public.autor_buch_id_seq'::regclass) NOT NULL,
    autor_id integer,
    buch_id integer
);
 "   DROP TABLE public.tbl_autor_buch;
       public         heap    postgres    false    215            �            1259    16409    tbl_buch    TABLE     �   CREATE TABLE public.tbl_buch (
    buch_id smallint NOT NULL,
    isbn bigint,
    titel character varying(80),
    subgen_id smallint,
    verlag character varying(40),
    veroffentlichungsdatum date,
    preis numeric(4,2)
);
    DROP TABLE public.tbl_buch;
       public         heap    postgres    false            �            1259    16412 	   tbl_genre    TABLE     c   CREATE TABLE public.tbl_genre (
    genre_id smallint NOT NULL,
    genre character varying(25)
);
    DROP TABLE public.tbl_genre;
       public         heap    postgres    false            �            1259    16415    tbl_subgenre    TABLE     �   CREATE TABLE public.tbl_subgenre (
    subgen_id smallint NOT NULL,
    subgenre character varying(25),
    genre_id smallint
);
     DROP TABLE public.tbl_subgenre;
       public         heap    postgres    false            �          0    16402 	   tbl_autor 
   TABLE DATA           K   COPY public.tbl_autor (autor_id, name, nationalitat, genre_id) FROM stdin;
    public          postgres    false    218   k!       �          0    16405    tbl_autor_buch 
   TABLE DATA           J   COPY public.tbl_autor_buch (autor_buch_id, autor_id, buch_id) FROM stdin;
    public          postgres    false    219   s"       �          0    16409    tbl_buch 
   TABLE DATA           j   COPY public.tbl_buch (buch_id, isbn, titel, subgen_id, verlag, veroffentlichungsdatum, preis) FROM stdin;
    public          postgres    false    220   #       �          0    16412 	   tbl_genre 
   TABLE DATA           4   COPY public.tbl_genre (genre_id, genre) FROM stdin;
    public          postgres    false    221   U&       �          0    16415    tbl_subgenre 
   TABLE DATA           E   COPY public.tbl_subgenre (subgen_id, subgenre, genre_id) FROM stdin;
    public          postgres    false    222   �&       �           0    0    autor_buch_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.autor_buch_id_seq', 42035, true);
          public          postgres    false    215            �           0    0    autor_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.autor_id_seq', 25011, true);
          public          postgres    false    216            �           0    0    buch_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.buch_id_seq', 17023, true);
          public          postgres    false    217            0           2606    16419 "   tbl_autor_buch tbl_autor_buch_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.tbl_autor_buch
    ADD CONSTRAINT tbl_autor_buch_pkey PRIMARY KEY (autor_buch_id);
 L   ALTER TABLE ONLY public.tbl_autor_buch DROP CONSTRAINT tbl_autor_buch_pkey;
       public            postgres    false    219            .           2606    16421    tbl_autor tbl_autor_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.tbl_autor
    ADD CONSTRAINT tbl_autor_pkey PRIMARY KEY (autor_id);
 B   ALTER TABLE ONLY public.tbl_autor DROP CONSTRAINT tbl_autor_pkey;
       public            postgres    false    218            2           2606    16423    tbl_buch tbl_buch_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tbl_buch
    ADD CONSTRAINT tbl_buch_pkey PRIMARY KEY (buch_id);
 @   ALTER TABLE ONLY public.tbl_buch DROP CONSTRAINT tbl_buch_pkey;
       public            postgres    false    220            4           2606    16425    tbl_genre tbl_genre_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.tbl_genre
    ADD CONSTRAINT tbl_genre_pkey PRIMARY KEY (genre_id);
 B   ALTER TABLE ONLY public.tbl_genre DROP CONSTRAINT tbl_genre_pkey;
       public            postgres    false    221            6           2606    16427    tbl_subgenre tbl_subgenre_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.tbl_subgenre
    ADD CONSTRAINT tbl_subgenre_pkey PRIMARY KEY (subgen_id);
 H   ALTER TABLE ONLY public.tbl_subgenre DROP CONSTRAINT tbl_subgenre_pkey;
       public            postgres    false    222            8           2606    16428    tbl_autor_buch fk_autor_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_autor_buch
    ADD CONSTRAINT fk_autor_id FOREIGN KEY (autor_id) REFERENCES public.tbl_autor(autor_id);
 D   ALTER TABLE ONLY public.tbl_autor_buch DROP CONSTRAINT fk_autor_id;
       public          postgres    false    218    219    4654            9           2606    16433    tbl_autor_buch fk_buch_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_autor_buch
    ADD CONSTRAINT fk_buch_id FOREIGN KEY (buch_id) REFERENCES public.tbl_buch(buch_id);
 C   ALTER TABLE ONLY public.tbl_autor_buch DROP CONSTRAINT fk_buch_id;
       public          postgres    false    4658    219    220            ;           2606    16438    tbl_subgenre fk_genre_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_subgenre
    ADD CONSTRAINT fk_genre_id FOREIGN KEY (genre_id) REFERENCES public.tbl_genre(genre_id);
 B   ALTER TABLE ONLY public.tbl_subgenre DROP CONSTRAINT fk_genre_id;
       public          postgres    false    221    222    4660            7           2606    16443    tbl_autor fk_genre_id    FK CONSTRAINT        ALTER TABLE ONLY public.tbl_autor
    ADD CONSTRAINT fk_genre_id FOREIGN KEY (genre_id) REFERENCES public.tbl_genre(genre_id);
 ?   ALTER TABLE ONLY public.tbl_autor DROP CONSTRAINT fk_genre_id;
       public          postgres    false    221    218    4660            :           2606    16448    tbl_buch fk_sugben_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_buch
    ADD CONSTRAINT fk_sugben_id FOREIGN KEY (subgen_id) REFERENCES public.tbl_subgenre(subgen_id);
 ?   ALTER TABLE ONLY public.tbl_buch DROP CONSTRAINT fk_sugben_id;
       public          postgres    false    4662    222    220            �   �   x�u�MN�0���s�*I[~��(�RV�6&+�1��Vp#.�z1\W"��|~�9_�i
�U2`E�����=Y=(Ѯ�!K�@2�M/�Q�aC#1�����h!�p����L>f��\$y$K(uH�'����r[AM��V��ɑ��dD���陴@A���W���'�J�ঀe�P�=9,�	���/_�Tƪ��;XI����co��m�l�Elt��,��f�J��w�e�"�~Voϓg�y�$�7���      �   �   x�Mл1��T��]�{q�u�4
̌x1��x�#�h�wi>��@�8����"-�iHOґ��L2��d!��>��܎�f��Ь�<�U�Ь��f��Ьۼ�u�7B�hk�f�$4;�b�M���4�IhvMR��SJ�f�I�      �   5  x����N�:���Sx ȿ�}ٖ9t�a@S��̍��C�+�L�۟m�� ���Tj�����L!���0͘B�������(CW6��E��G�PVSQ��87����P.GϝC���΁�Ȋ�
�D�(`CEÉь|�����M�@�s%3��\'Z5��G��p�?):i�|JJʔ���Ǿ�LH��O�=�}j>��e��1��pt�����@4�Z)$����v��0_�ߵ�A+�+N�#Be�Q����ʿ�o	��|���zօ�0�"�K=�i��3D��`f�0�)�k]�q�oC��.�C��%�6����7��ch��lKu�{�S2�kΌB���U���_��:�?���fׄ���.�?>����=~X��5F���Z���Z�-^��\��	?B«�Y-���:|u��\�v8Z�e���}�B<����C����}B���1�����#F���੻��C9�;l���7`�	�N�l�q9��Ԑ�*�la����v{���ӄ~�� D�����ߨ<5*���Z�e̐�����]�_gh��~�n
&�G«󕩍PZ�W�Ф_ز�Ut6��e�*�{p���m�k��>m�nIMn���{(�f,S�A��J���Ƶ��o�;�d �����Q|S���e�t���,Y!�(�5W]�ե�-�������&*��.cF T�m�z��ۥ�CH���X�ad��^����s#����r��#B	^�!�Hg~C���z;�o�c��TBhđ�o)+��V��Pn|�4����@p7��&O�i�G��>?;;��I��      �   <   x�3�t�L.����2����KI-�2��,.N�+N�HL+��L��2���/*�/����� ���      �   �   x��A
1E��)��B3s���nܔm��J���7�bv�/�~pMx?Kr�
��c[{� 'u���|����_g�fp�Z�߹_���MZcm)ǇI�w��,\�<��5��٤6q$8V�-��]�����1�     