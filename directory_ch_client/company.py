from directory_ch_client.base import BaseCHClient


class CompanyCHClient(BaseCHClient):

    endpoints = {
        'search-companies': '/api/search/companies/',
        'registered-address':
            '/api/company/{company_number}/registered-office-address/',
        'profile': '/api/company/{company_number}/'
    }

    def search_companies(self, query):
        return self.get(
            self.endpoints['search-companies'],
            params={'q': query}
        )

    def get_company_registered_address(self, company_number):
        url = self.endpoints['registered-address'].format(
            company_number=company_number
        )
        return self.get(url)

    def get_company_profile(self, company_number):
        url = self.endpoints['profile'].format(
            company_number=company_number
        )
        return self.get(url)
