import { Loader2, WandSparkles } from 'lucide-react';

type Props = {
  prompt: string;
  style: string;
  loading: boolean;
  onPromptChange: (value: string) => void;
  onStyleChange: (value: string) => void;
  onGenerate: () => void;
};

const styles = [
  'realistic',
  'cinematic',
  'anime',
  'digital art',
  '3D render',
  'logo design',
  'marketing banner',
];

export function CreatorPanel({ prompt, style, loading, onPromptChange, onStyleChange, onGenerate }: Props) {
  return (
    <section className="panel creatorPanel">
      <div className="sectionTitle">
        <WandSparkles size={22} />
        <h2>Create</h2>
      </div>

      <label>Prompt</label>
      <textarea
        value={prompt}
        onChange={(event) => onPromptChange(event.target.value)}
        placeholder="Example: A futuristic AI design studio in New York with holographic screens"
      />

      <label>Creative Mode</label>
      <select value={style} onChange={(event) => onStyleChange(event.target.value)}>
        {styles.map((item) => (
          <option key={item} value={item}>{item}</option>
        ))}
      </select>

      <button onClick={onGenerate} disabled={loading || !prompt.trim()}>
        {loading ? <Loader2 className="spin" size={18} /> : <WandSparkles size={18} />}
        {loading ? 'Generating...' : 'Generate Image'}
      </button>

      <div className="note">
        This version uses a production-style workflow with placeholder image output. Real AI model integration comes in Part 2/3.
      </div>
    </section>
  );
}
