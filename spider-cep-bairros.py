import scrapy

class CepBairrosSpider(scrapy.Spider):
    name = 'cep-bairros-spider'
    start_urls = ['http://www.buscacep.correios.com.br/sistemas/buscacep/buscaLogBairro.cfm']
    form_url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaLogBairro.cfm'
    total_per_page = 50
    last_item = 0

    def get_form_data(self):
        return {
            'UF': self.uf,
            'Localidade': self.localidade,
            'Bairro': self.bairro,
            'qtdrow': str(self.total_per_page),
            'pagini': str(self.last_item),
            'pagfim': str(self.last_item + self.total_per_page)
        }

    def parse (self, response):
        url = response.css('form::attr(action)').extract_first()

        data = self.get_form_data()
        yield scrapy.FormRequest(url=self.form_url, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        for q in response.css('table.tmptabela tr'):
            columns = q.css('td');

            if not columns:
                continue

            yield {
                'nome': columns[0].css('::text').extract_first(),
                'bairro': columns[1].css('::text').extract_first(),
                'cep': columns[3].css('::text').extract_first() 
            }
        
        next_page_form = response.css('form[name="Proxima"]')

        if not next_page_form:
            return

        self.last_item = self.last_item + self.total_per_page + 1;

        yield scrapy.FormRequest(url=self.form_url, formdata=self.get_form_data(), callback=self.parse_page)