import { ImageIcon } from 'lucide-react';
import type { ImageRecord } from '../types/image';

type Props = { image: ImageRecord | null };

export function PreviewPanel({ image }: Props) {
  return (
    <section className="panel previewPanel">
      <div className="sectionTitle">
        <ImageIcon size={22} />
        <h2>Latest Result</h2>
      </div>

      {image ? (
        <div className="previewContent">
          <img src={image.image_url} alt={image.prompt} />
          <div className="metadata">
            <span>{image.style}</span>
            <span>{image.status}</span>
          </div>
          <h3>Enhanced Prompt</h3>
          <p>{image.enhanced_prompt}</p>
        </div>
      ) : (
        <div className="emptyState">
          <ImageIcon size={52} />
          <p>Your generated image will appear here.</p>
        </div>
      )}
    </section>
  );
}
