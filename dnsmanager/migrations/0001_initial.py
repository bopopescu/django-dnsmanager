# Generated by Django 2.2.3 on 2019-12-18 14:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import dnsmanager.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=253, verbose_name='name')),
                ('dns_class', models.CharField(choices=[('IN', 'IN (Internet)'), ('CS', 'CS (CSNET, obsolete)'), ('CH', 'CH (CHAOS)'), ('HS', 'HS (Hesiod)')], default='IN', help_text="You shouldn't need anything else than IN.", max_length=2, verbose_name='class')),
                ('ttl', models.PositiveIntegerField(default=3600, help_text='Limits the lifetime of this record.', null=True, verbose_name='Time To Live')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_dnsmanager.record_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'record',
                'verbose_name_plural': 'records',
                'ordering': ['zone', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', dnsmanager.fields.DomainNameField(unique=True, verbose_name='name')),
                ('slug', models.SlugField(help_text='This zone will be accessible at /dns/{slug}/.', max_length=253, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'zone',
                'verbose_name_plural': 'zones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AddressRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('address', models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4 address')),
            ],
            options={
                'verbose_name': 'A record',
                'verbose_name_plural': 'A records',
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='CanonicalNameRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('c_name', models.CharField(help_text='This domain name will alias to this canonical name.', max_length=253, verbose_name='canonical name')),
            ],
            options={
                'verbose_name': 'CNAME record',
                'verbose_name_plural': 'CNAME records',
                'ordering': ['c_name'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='CertificationAuthorityAuthorizationRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('flags', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)], verbose_name='flags')),
                ('tag', models.CharField(choices=[('issue', 'issue'), ('issuewild', 'issue wildcard'), ('iodef', 'Incident object description exchange format')], max_length=255, verbose_name='tag')),
                ('value', models.CharField(max_length=511, verbose_name='value')),
            ],
            options={
                'verbose_name': 'CAA record',
                'verbose_name_plural': 'CAA records',
                'ordering': ['flags'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='DelegationNameRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('d_name', dnsmanager.fields.DomainNameField(help_text='This domain name will alias to the entire subtree of that delegation domain.', verbose_name='delegation domain name')),
            ],
            options={
                'verbose_name': 'DNAME record',
                'verbose_name_plural': 'DNAME records',
                'ordering': ['d_name'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='Ipv6AddressRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('address', models.GenericIPAddressField(protocol='IPv6', verbose_name='IPv6 address')),
            ],
            options={
                'verbose_name': 'AAAA record',
                'verbose_name_plural': 'AAAA records',
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='MailExchangeRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('preference', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='preference')),
                ('exchange', dnsmanager.fields.DomainNameField(default='@', verbose_name='exchange server')),
            ],
            options={
                'verbose_name': 'MX record',
                'verbose_name_plural': 'MX records',
                'ordering': ['preference'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='NameServerRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('nsdname', dnsmanager.fields.DomainNameField(default='@', verbose_name='name server')),
            ],
            options={
                'verbose_name': 'NS record',
                'verbose_name_plural': 'NS records',
                'ordering': ['nsdname'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='PointerRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('ptrdname', dnsmanager.fields.DomainNameField(verbose_name='pointer domain name')),
            ],
            options={
                'verbose_name': 'PTR record',
                'verbose_name_plural': 'PTR records',
                'ordering': ['ptrdname'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('priority', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='priority')),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='weight')),
                ('port', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)], verbose_name='port')),
                ('target', dnsmanager.fields.DomainNameField(verbose_name='target')),
            ],
            options={
                'verbose_name': 'SRV record',
                'verbose_name_plural': 'SRV records',
                'ordering': ['priority', 'target'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='SshFingerprintRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('algorithm', models.PositiveIntegerField(choices=[(1, 'RSA'), (2, 'DSA'), (3, 'ECDSA'), (4, 'Ed25519')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='algorithm')),
                ('type', models.PositiveIntegerField(choices=[(1, 'SHA-1'), (2, 'SHA-256')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='type')),
                ('fingerprint', models.CharField(max_length=64, verbose_name='fingerprint')),
            ],
            options={
                'verbose_name': 'SSHFP record',
                'verbose_name_plural': 'SSHFP records',
                'ordering': ['algorithm'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='StartOfAuthorityRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('mname', dnsmanager.fields.DomainNameField(help_text='Primary master name server for this zone.', verbose_name='master name server')),
                ('rname', models.EmailField(help_text='Email address of the administrator responsible for this zone.', max_length=254, verbose_name='responsible email')),
                ('serial', models.BigIntegerField(help_text='A slave name server will initiate a zone transfer if this serial is incremented.', verbose_name='serial number')),
                ('refresh', models.BigIntegerField(default=86400, help_text='Number of seconds after which secondary name servers should query the master to detect zone changes.', verbose_name='refresh')),
                ('retry', models.BigIntegerField(default=7200, help_text='Number of seconds after which secondary name servers should retry to request the serial number from the master if the master does not respond.', verbose_name='retry')),
                ('expire', models.BigIntegerField(default=3600000, help_text='Number of seconds after which secondary name servers should stop answering request for this zone if the master does not respond.', verbose_name='expire')),
                ('minimum', models.BigIntegerField(default=172800, help_text='Time to live for purposes of negative caching.', verbose_name='minimum')),
            ],
            options={
                'verbose_name': 'SOA record',
                'verbose_name_plural': 'SOA records',
                'ordering': ['mname'],
            },
            bases=('dnsmanager.record',),
        ),
        migrations.CreateModel(
            name='TextRecord',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dnsmanager.Record')),
                ('data', models.TextField()),
            ],
            options={
                'verbose_name': 'TXT record',
                'verbose_name_plural': 'TXT records',
            },
            bases=('dnsmanager.record',),
        ),
        migrations.AddField(
            model_name='record',
            name='zone',
            field=models.ForeignKey(help_text='This record will be applied on that zone.', on_delete=django.db.models.deletion.CASCADE, to='dnsmanager.Zone', verbose_name='zone'),
        ),
    ]
