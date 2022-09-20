# Generated by Django 4.1.1 on 2022-09-20 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('perfil', models.CharField(max_length=50, verbose_name='Perfil')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('celular', models.CharField(max_length=13, verbose_name='Celular')),
                ('genero', models.CharField(max_length=1, verbose_name='Genero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fecha_nac', models.DateField(verbose_name='Fecha Nacimiento')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('idSignoVital', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=100, verbose_name='Oximetria')),
                ('frec_respiratoria', models.CharField(max_length=100, verbose_name='Frecuencia Respiratoria')),
                ('frec_cardiaca', models.CharField(max_length=1# Generated by Django 4.1.1 on 2022-09-20 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('perfil', models.CharField(max_length=50, verbose_name='Perfil')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('celular', models.CharField(max_length=13, verbose_name='Celular')),
                ('genero', models.CharField(max_length=1, verbose_name='Genero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fecha_nac', models.DateField(verbose_name='Fecha Nacimiento')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('idSignoVital', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=100, verbose_name='Oximetria')),
                ('frec_respiratoria', models.CharField(max_length=100, verbose_name='Frecuencia Respiratoria')),
                ('frec_cardiaca', models.CharField(max_length=100, verbose_name='Frecuencia Cardiaca')),
                ('temperatura', models.CharField(max_length=100, verbose_name='Temperatura')),
                ('glicemias', models.CharField(max_length=100, verbose_name='Glicemias')),
                ('presion_arterial', models.CharField(max_length=100, verbose_name='Presion Arterial')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y Hora')),
                ('paciente_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signoVital', to='saludApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalSalud',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('rol', models.CharField(max_length=100, verbose_name='Rol')),
                ('especialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pSalud', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='pSalud_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='saludApp.personalsalud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id_historia_cl', models.AutoField(primary_key=True, serialize=False)),
                ('sugerencias', models.CharField(max_length=500, verbose_name='Sugerencias')),
                ('diagnostico', models.CharField(max_length=500, verbose_name='Diagnostico')),
                ('entorno', models.CharField(max_length=500, verbose_name='Entorno')),
                ('fecha_sug', models.DateField(verbose_name='Fecha Sugerencia')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripción')),
                ('paciente_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiaClinica', to='saludApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('documento', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('parentesco', models.CharField(max_length=100, verbose_name='Parentesco')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo')),
                ('paciente_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='saludApp.paciente')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
