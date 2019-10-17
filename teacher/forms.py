from django import forms
from django.utils.translation import gettext as _

from .models import School

class SchoolSearchForm(forms.Form):
    name = forms.CharField(label=_('School name'), required=False)
    city = forms.CharField(label=_('City'), required=False)
    state = forms.CharField(label=_('State (abbreviation)'), required=False, max_length=2)
    zip = forms.CharField(label=_('ZIP'), required=False, max_length = 5)

class AddSchoolForm(forms.Form):
    name = forms.CharField(label=_('School name'))
    address = forms.CharField(label=_('Address'))
    city = forms.CharField(label=_('City'))
    state = forms.CharField(label=_('State / Province / Region (abbreviation)'), required=False, max_length=2)
    zip = forms.CharField(label=_('ZIP / Postal code'), required=False, max_length = 10)
    country_choices = (('', ''),('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua And Barbuda', 'Antigua And Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia And Herzegovina', 'Bosnia And Herzegovina'), ('Botswana', 'Botswana'), ('Bouvet Island', 'Bouvet Island'), ('Brazil', 'Brazil'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos Islands', 'Cocos Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('The Democratic Republic Of The Congo', 'The Democratic Republic Of The Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote D\'ivoire', 'Cote D\'ivoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French Southern Territories', 'French Southern Territories'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-bissau', 'Guinea-bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Heard Island And Mcdonald Islands', 'Heard Island And Mcdonald Islands'), ('Holy See', 'Holy See'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Islamic Republic Of Iran', 'Islamic Republic Of Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakstan', 'Kazakstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Democratic People\'s Republic Of Korea', 'Democratic People\'s Republic Of Korea'), ('Republic Of Korea,', 'Republic Of Korea,'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('The Former Yugoslav Republic Of Macedonia', 'The Former Yugoslav Republic Of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Federated States Of Micronesia', 'Federated States Of Micronesia'), ('Republic Of Moldova', 'Republic Of Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montserrat', 'Montserrat'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('Netherlands Antilles', 'Netherlands Antilles'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('State of Palestine', 'State of Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Helena', 'Saint Helena'), ('Saint Kitts And Nevis', 'Saint Kitts And Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Pierre And Miquelon', 'Saint Pierre And Miquelon'), ('Saint Vincent And The Grenadines', 'Saint Vincent And The Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome And Principe', 'Sao Tome And Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Georgia And The South Sandwich Islands', 'South Georgia And The South Sandwich Islands'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Svalbard And Jan Mayen', 'Svalbard And Jan Mayen'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Taiwan, Province Of China', 'Taiwan, Province Of China'), ('Tajikistan', 'Tajikistan'), ('United Republic Of Tanzania', 'United Republic Of Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad And Tobago', 'Trinidad And Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks And Caicos Islands', 'Turks And Caicos Islands'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States of America', 'United States of America'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Viet Nam', 'Viet Nam'), ('British Virgin Islands', 'British Virgin Islands'), ('U.S. Virgin Islands', 'U.S. Virgin Islands'), ('Wallis And Futuna', 'Wallis And Futuna'), ('Western Sahara', 'Western Sahara'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'))
    country = forms.ChoiceField(label=_('Country'), choices=country_choices)
    confirmed = forms.BooleanField(widget = forms.HiddenInput(), initial=False, required=False)

class SettingsForm(forms.Form):
    code = forms.CharField(label=_('School staff code'))
    
    def clean_code(self):
        code = self.cleaned_data.get('code')
        try:
            school = School.objects.get(code = code)
        except:
            raise forms.ValidationError(
                _('That school code is not valid, please try another.'),
            )
        return code