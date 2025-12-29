import json
import os

def generate_markdown(roadmap):
    """Converts a single roadmap dictionary into a Markdown string."""
    md = f"# {roadmap['title']}\n\n"
    md += f"_{roadmap['description']}_\n\n"
    md += "---\n\n"
    md += "> **⚠️ Not:** Bu dosya `roadmap.json` kaynak alınarak otomatik oluşturulmuştur. Lütfen doğrudan düzenlemeyiniz.\n\n"

    for level in roadmap['levels']:
        md += f"## 📍 Seviye {level['level']}: {level['name']}\n\n"
        
        md += "### 🎯 Öğrenilecek Konular\n"
        for topic in level['topics']:
            md += f"- [ ] {topic}\n"
        md += "\n"

        md += "### 📚 Önerilen Kaynaklar\n"
        for resource in level['resources']:
            type_badge = f"![Badge](https://img.shields.io/badge/{resource['type']}-blue?style=flat-square)"
            md += f"- {type_badge} [{resource['title']}]({resource['url']})\n"
        
        md += "\n---\n\n"
    
    return md

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'curriculum', 'roadmap.json')
    output_dir = os.path.join(base_dir, 'curriculum', 'pathways')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"🚀 Roadmap yüklendi. Bulunan yol haritası sayısı: {len(data['roadmaps'])}")

        for roadmap in data['roadmaps']:
            filename = f"{roadmap['id']}.md"
            filepath = os.path.join(output_dir, filename)
            
            markdown_content = generate_markdown(roadmap)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated: {filepath}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
