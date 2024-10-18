import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class FazendaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Adiciona um título
        layout.add_widget(Label(text="Lista de Fazendas"))

        # Cria um ScrollView para permitir rolar as fazendas
        scroll_view = ScrollView()
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # Faz uma requisição GET para o backend Django e busca as fazendas
        try:
            response = requests.get('http://127.0.0.1:8000/api/fazendas/')
            print(f"Status Code: {response.status_code}")  # Aqui está o print que você pode usar
            if response.status_code == 200:
                fazendas = response.json()
                for fazenda in fazendas:
                    label = Label(text=f'{fazenda["nome"]}: {fazenda["tamanho"]} hectares', size_hint_y=None, height=40)
                    scroll_layout.add_widget(label)
            else:
                scroll_layout.add_widget(Label(text="Erro ao buscar fazendas"))
        except requests.exceptions.RequestException as e:
            scroll_layout.add_widget(Label(text=f"Erro de conexão: {e}"))

        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)

        # Botão de sair
        button = Button(text="Sair", size_hint=(1, None), height=40)
        button.bind(on_press=self.stop)  # Fecha o aplicativo ao clicar no botão
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    FazendaApp().run()
